import speech_recognition
import pyttsx3

from datetime import date,datetime


robot_mouth = pyttsx3.init()
robot_brain= ""
robot_ear = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print("robot:I'm listening...")
        audio =  robot_ear.listen(mic) 
    try:
        you = robot_ear.recognize_google(audio)
        
    except:
        you = ""
        
    print("you:"+you)


    if you == "":
        print("i can't hear you,try again")

    elif  "hello" in you:
        robot_brain = "hello tien anh"
    elif  "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")

    elif  "time" in you :
        now=datetime.now()
        robot_brain=now.strftime("%H hours %M minutes %S seconds")


    elif "love me" in you:
        robot_brain ="i love you "
    elif "President" in you:
        robot_brain = "Vladimir Vladimirovich Putin"
    elif "bye" in you:
        robot_brain="bye tien anh"
        print("robot:"+robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "i'm fine thank you and you"

    print(robot_brain)
    voices = robot_mouth.getProperty('voices')  
    robot_mouth.setProperty('voice', voices[1].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
