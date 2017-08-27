
#Email using Python - Email Module

def SendMail():
    global tomail
    global message
    global username
    global password
    import smtplib
    server= smtplib.SMTP('smtp.gmail.com',587)
    try:
        server.starttls()
        server.login(username,password)
        server.sendmail(username,tomail,message)
        print("Email sent !")
    except:
        print("Can not send mail!")

tomail=""
message=""
username=""
password=""
print("Email through Python!")
print("______________________________________________")
print("Please enter your email address")
username=input()
print("Please enter your password")
password=input()
print("Please enter recipient email address")
tomail=input()
print("Please enter your message")
message=input()
print("_______________________________________________")
rep=input("Send Email? Y/N")
if rep=="Y" or rep=="y":
    SendMail()






    
