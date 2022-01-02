'''
Created on Jan 26, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

###############################################################3
#Testing Email Functionality 
from email.mime.multipart import MIMEMultipart #, MIMEImage, MIMEMessage
from email.mime.text import MIMEText
import smtplib, ssl


def main():
    FROM = "pythonCode"
    TO = "priyankachoudhary1@gmail.com"
    CC = "goyalpushkar@gmail.com"
    EVERYONE = TO + "," + CC
    
    USERNAME="cnswholesalegrocers" 
    PSWD=raw_input("Enter Gmail Pswd: ")   #input("Enter Gmail Pswd: ") 
      
    #print(PSWD)
    msg = MIMEMultipart()
    msg.add_header("From", FROM)
    msg.add_header("To", TO)
    msg.add_header("Cc", CC )
    msg.add_header("Subject", "Padhti Nahi")
    
    msgBodyText = """ Hi,
                  
                      Padhliya Kar.. Jaldi Utha Kar....Target Pure Kiya Kar
                  
                  Bhad Mein Jaa,
                  pythonCode
              """
    msgBodyHTML = """Hi Londki,<br>
                     <br>
                        <p>Padhliya Kar.. Jaldi Utha Kar....Target Pure Kiya Kar<br></p>
                        <p>PayPams Details: <br></p>
                        <p>UserName: goyalpushkar@gmail.com <br></p>
                        <p>Pswd: GarvLunch@27 <br></p>
                     <br>
                     Bhad Mein Jaa,<br>
                     pythonCode
              """
    msg.attach( MIMEText(msgBodyHTML,"html") )
    
    try:
        host = "smtp.gmail.com"
        port = 587  # For starttls
        server = smtplib.SMTP(host, port)
        
        sport = 465 # For SSL
        context = ssl.create_default_context()
        #sserver = smtplib.SMTP_SSL(host, sport, context)
        #with smtplib.SMTP_SSL(host, sport, context) as server:
        server.starttls()
        server.login(USERNAME, PSWD)
        #server.sendmail(USERNAME, CC, msgBody)
        server.sendmail(FROM, TO, msg.as_string())
        #sserver.send_message(msg)
        
        print("Email Sent")
    except Exception as e:
        print(e)
    finally:
        server.quit()    


if __name__ == '__main__':
    main()
