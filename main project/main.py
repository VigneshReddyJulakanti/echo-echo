#new #new 
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia # To acess wikipedia directly
import webbrowser
import os
import smtplib
import time
import selenium
from selenium import webdriver
# from selenium.webdriver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # used for  detaching  driver , bcoz of which the driver is not closed 
from selenium.webdriver.common.action_chains import ActionChains
from word2number import w2n
import cv2
from keras.models import load_model
import numpy as np
from pygame import mixer
import time




master="Vignesh"
myName="echo"
similarname1="eko"
DOB="8th january 2021"  #jarvis DOB

print(f"...........intializing  {myName}...............")
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning vignesh. Now the time is around {0} am".format(hour))
    elif hour<18:
        speak("Good afternoon vignesh. Now the time is around {0} pm".format(hour))
    elif hour<21 :
        speak("Good evening vignesh. Now the time is around {0} pm ".format(hour))
    else:
        speak("Good night vignesh. Now the time is around {0} pm , you better go to sleep .".format(hour))

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold=0.6
        audio=r.listen(source)
       

    try:
        #print("Recognition...")
        query=r.recognize_google(audio,language="en-in")
        #print(f"user said:{query}\n")

    except Exception as e:
        print("cant recognize u for a instance of 0.6 seconds")
        query= None
        mainif()

    return query


error=" Dirty fellow , idiot , buffalo  , waste fellow not having any common sense , you havent coded me any thing about this "
scoldme=" Dirty fellow , idiot , buffalo , waste fellow not having any common sense "

#Main programme starts
speak(f"{myName} intialized...")

wishme()
speak(" How may i help you?")
#query=0
#query=takecommand()
#print(query)

#Basic tasks

def mainif():
    

    query=takecommand()
    query=query.lower()
    print(query)
    if myName in query:
            query=query.replace(myName,"")

            # if "active" in query and "mode" in query:
            #     query=str(query)+myName
            #     mainif()

            # if "sleep" in query and "mode" in query:
            #     query=query.replace(myName,'')    

            if "introduce" in query:
                if ("introduce" and "your" and "self") :
                    speak(f" Helloo ... , I am {myName} , speed 2 giggahertz , memory half terabyte , I was created by Vignesh Reddy J , I am here to help him")
                    mainif()


            if ("join" in query and "class" in query) or ("open" in query and "class" in query): #KMIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://kmitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("Kmit123$")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                driver.implicitly_wait(50000)

                ele_join=driver.find_element_by_xpath("//*[@id='region-main']/div/div/div/div/div[3]/a/span").click()
                Options().add_experimental_option("detach",True)
                time.sleep(500)
                speak("opened")
                mainif()


            elif ( "speakout" in query and "table" in query) or ( "speak out" in query and "table" in query) :
                query=query.replace("speak","")
                query=query.replace("out","")

                query=query.replace("table","")
                query=query.replace(" ","")
                # query.replace("se","")
                print(query)
                if (query.isdigit()):
                    t=int(query)
                    speak   (    
                            f"{t} into 1 , {t*1}   , "
                            f"{t} into 2 , {t*2}   , "
                            f"{t} into 3 , {t*3}   , "
                            f"{t} into 4 , {t*4}   , "
                            f"{t} into 5 , {t*5}   , "
                            f"{t} into 6 , {t*6}   , "
                            f"{t} into 7 , {t*7}   , "
                            f"{t} into 8 , {t*8}   , "
                            f"{t} into 9 , {t*9}   , "
                            f"{t} into 10 , {t*10} , " 
                            )
                else:
                    query=w2n.word_to_num(query)
                    t=0
                    t=int(query)
                    speak (    
                        f"{t} into 1 , {t*1}   , "
                        f"{t} into 2 , {t*2}   , "
                        f"{t} into 3 , {t*3}   , "
                        f"{t} into 4 , {t*4}   , "
                        f"{t} into 5 , {t*5}   , "
                        f"{t} into 6 , {t*6}   , "
                        f"{t} into 7 , {t*7}   , "
                        f"{t} into 8 , {t*8}   , "
                        f"{t} into 9 , {t*9}   , "
                        f"{t} into 10 , {t*10} ,   "
                )
                mainif()
            
            elif "hello" in query:
                speak("hlo {0}".format(master))
                mainif()

            elif "your" in query and "name" in query:
                speak("My name is {0}".format(myName))
                mainif()
        
            elif "your" in query and "date" in query and "birth" in query:
                speak("I am initially initialized on {0}".format(DOB))
                mainif()

            elif "when"in query and "born" in query:
                speak("I am initially initialized on {0}".format(DOB))
                mainif()
                

            elif "open"in query and "python"in query and "ppt"in query and "page" in query: #NGIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://ngitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("8309882962@")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                ele_studyMaterialPage=driver.find_element_by_xpath("//*[@id='region-main']/div/div/ul/li[6]/a").click()
                ele_kmit=driver.find_element_by_xpath("//*[@id='KMIT_anchor']")
                ActionChains(driver).double_click(ele_kmit).perform()

                ele_firstYear=driver.find_element_by_xpath("//*[@id='KMIT/1st-year_anchor']")
                ActionChains(driver).double_click(ele_firstYear).perform()

                ele_ppt=driver.find_element_by_xpath("//*[@id='KMIT/1st-year/PPT_anchor']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()

            elif "open"in query and "tessellator"in query and "ngit" in query: #NGIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://ngitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("8309882962@")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
                
            elif "open"in query and "tessellator" in query: #KMIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://kmitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("20BD1A055T") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("Kmit123$")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
                

            elif ("open google") in  query:
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window()
                driver.get("https://www.google.com/")
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()

            elif ("google") in query:
                speak("opening")
                if myName in query:
                    query=query.replace(myName,"")
                query=query.replace("google","")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window()
                driver.get("https://www.google.com/")
                ele_search=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                ele_search.send_keys(query)
                ele_search.send_keys(Keys.ENTER)
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()

            elif "what is" in query:    #if "what is " there in our query then it will execute this function
                speak("opening")
                query=query.replace("what is","")
                results=wikipedia.summary(query,sentences=2)
                speak(results)
                mainif()

            elif "calculate"  in query or "add" in query  or "subtract" in query or "multiply"  in query : #This uses eval function when our query involves the word calculate
                if "calculate" in query:
                    query=query.replace("calculate","")
                    if "into" in query:
                            query=query.replace("into","*")
                            query=eval(query)
                            speak(query) 
                            
                
                    else :
                        query=eval(query)
                        speak(query)
                    mainif()
                
                if "add" in query:
                    query=query.replace("add","")
                    query=eval(query)
                    speak(query)
                    mainif()
                if "subtract" in query:
                    query=query.replace("subtract","")
                    query=eval(query)
                    speak(query)
                    mainif()

                if "multiply" in query:
                    if "into" in query:
                            query=query.replace("into","*")
                            query=eval(query)
                            speak(query)
                            mainif()

            elif "wastefellow" in query: #is ... a waste fellow
                query=query.replace("a waste fellow","")
                query=query.replace("is","")
                speak(" Dirty fellow {0}, idiot {0} , buffalo {0}, waste fellow {0} not having any common sense ".format(query))
                time.sleep(1)
                mainif()
                
            elif "waste fellow" in query: #is ... a waste fellow
                query=query.replace("a waste fellow","")
                query=query.replace("is","")
                speak(" Dirty fellow {0}, idiot {0} , buffalo {0}, waste fellow {0} not having any common sense ".format(query))
                time.sleep(1)
                mainif()

            elif "the time" in query:
                strtime=datetime.datetime.now().strftime("%H:%M")
                speak(f"The , time is {strtime}")
                time.sleep(1)
                mainif()

            elif "open youtube" in query:#opens youtube 
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("https://www.youtube.com/?feature=ytca")
                speak("opened")           
                mainif()

            elif "open whatsapp" in query:#opens youtube 
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                # driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("https://web.whatsapp.com/")
                speak("opened")
                mainif()

            elif "open" in query  and "vs code" in query:
                speak("opening")
                codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codepath)
                speak("opened")
                mainif()
            
            elif "hai" in query:
                speak(" hai {0}".format(master))
                mainif()

            elif "ask" in query  and "me" in query  and "question" in query:
                speak("{0} why dont you get any idea?".format(master))
                mainif()

            elif "say" in query  and "why" in query:
                speak("you are not having any brain , that the reason ")
                mainif()
            
            elif "sleep" in query:
                speak("ok bye {0}.".format(master))
                
            elif "sleepmode" in query:
                speak("ok bye {0}.".format(master))

            elif "thank you" in query:
                speak("ok bye {0}.".format(master))

            elif "bye" in query:
                speak("ok bye {0}.".format(master))

            elif ("update" and "yourself") in query:
                        
                with open("‪\\..\\..\\..\\Python\\jarvis\\main.py") as f:
                    newcontent=f.read()

                with open("\\..\\..\\..\\Users\\DELL\\main.py","w") as f:
                    f.write(newcontent)

                speak("updated succesfully")


            elif ("study" in query) and  ("mode" in query) and ("on" in query):
                                
                mixer.init()
                sound = mixer.Sound('alarm.wav')
                echo_sound=mixer.Sound('echo_sound.wav')

                face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
                leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
                reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')

                lbl=['Close','Open']

                model = load_model('models/cnncat2.h5')
                path = os.getcwd()
                cap = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                count=0
                score=0
                thicc=2
                rpred=[99]
                lpred=[99]

                while(True):
                    ret, frame = cap.read()
                    height,width = frame.shape[:2] 

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
                    left_eye = leye.detectMultiScale(gray)
                    right_eye =  reye.detectMultiScale(gray)

                    cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

                    for (x,y,w,h) in faces:
                        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )

                    for (x,y,w,h) in right_eye:
                        r_eye=frame[y:y+h,x:x+w]
                        count=count+1
                        r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                        r_eye = cv2.resize(r_eye,(24,24))
                        r_eye= r_eye/255
                        r_eye=  r_eye.reshape(24,24,-1)
                        r_eye = np.expand_dims(r_eye,axis=0)
                        rpred = model.predict_classes(r_eye)
                        if(rpred[0]==1):
                            lbl='Open' 
                        if(rpred[0]==0):
                            lbl='Closed'
                        break

                    for (x,y,w,h) in left_eye:
                        l_eye=frame[y:y+h,x:x+w]
                        count=count+1
                        l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                        l_eye = cv2.resize(l_eye,(24,24))
                        l_eye= l_eye/255
                        l_eye=l_eye.reshape(24,24,-1)
                        l_eye = np.expand_dims(l_eye,axis=0)
                        lpred = model.predict_classes(l_eye)
                        if(lpred[0]==1):
                            lbl='Open'   
                        if(lpred[0]==0):
                            lbl='Closed'
                        break

                    if(rpred[0]==0 and lpred[0]==0):
                        score=score+1
                        cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                    # if(rpred[0]==1 or lpred[0]==1):
                    else:
                        score=score-1
                        cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                       
                    if(score<0):
                        score=0   
                    cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                    if(score>30):
                        #person is feeling sleepy so we beep the alarm
                        cv2.putText(frame, 
                                    "Echo Echo dont sleep", (70,70),
                                    cv2.FONT_HERSHEY_PLAIN, 3,
                                    (0,0,255),2)
                        cv2.imwrite(os.path.join(path,'image.jpg'),frame)
                        try:
                            # sound.play()
                            echo_sound.play()
                            
                        except:  # isplaying = False
                            pass
                        if(thicc<16):
                            thicc= thicc+2
                        else:
                            thicc=thicc-2
                            if(thicc<2):
                                thicc=2
                        cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc) 
                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
                        
                mainif()

            else:
                mainif()       

    else:
        mainif()
   
mainif()

