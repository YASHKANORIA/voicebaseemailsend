import smtplib as smtp
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

email_list = {
    'anjali' :'anjalirathi94@gmail.com',
    'yash' : 'yashbattu@gmail.com',
    'shubham':'ksubham.sharma@gmail.com',
    'mohit' :'yshkanoria@hotmail.com'
}
print(email_list)
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()



listener = sr.Recognizer()

def email_information():
    try:
        with sr.Microphone() as source:
            print("Bol bhai")
            voice = listener.listen(source)
            voicetotext=listener.recognize_google(voice)
            print(voicetotext)
            return voicetotext.lower()

    except:
        pass
        print("unble")

def sendmail(receiver,body):

    server = smtp.SMTP('smtp.gmail.com' ,   587)

    server.starttls()
    server.login('workyashkanoria@gmail.com','****************')
    email=EmailMessage()
    email['From']='workyashkanoria@gmail.com'
    email['To']=receiver
    email['Subject']=subject
    email.set_content(body)
    server.send_message(email)

def get_info_for_email():
    talk("Reciver Mail Address :")
    receiver = email_information()
    gmail=email_list[receiver]
    print("-----------------------------------")
    print(gmail)
    talk("Subject to be")
    subject=email_information()
    talk("message ")
    message = email_information()

    sendmail(gmail,message)

get_info_for_email()
