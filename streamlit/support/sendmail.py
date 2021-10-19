import smtplib
from email.message import EmailMessage

Sender_Email = "wepefa6009@omibrown.com"
Reciever_Email = "peresj.developer@gmail.com"
Password = input('Enter your email account password: ')

newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from CodeItBro" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email
newMessage.set_content('Hi, hope you are doing fine! Stay Home! Stay Safe!') #Defining email body


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password) #Login to SMTP server
    smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object