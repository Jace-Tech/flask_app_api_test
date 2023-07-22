from flask import Flask
from flask_mail import Mail, Message
from dotenv import dotenv_values

ENV = dotenv_values() 

def send_mail(app: Flask, subject: str, recipients, body: str, is_html: bool = False):
  """
    Sends email message to recipients
  """
  mail = Mail(app)
  try:
    sender = (ENV['APP_NAME'], ENV["MAIL_USERNAME"])
    message = Message(subject, recipients, html=body, sender=sender) \
      if is_html \
      else Message(subject, recipients, body, sender=sender)
    
    # SEND EMAIL
    mail.send(message)

    # RETURN TRUE
    return True
  
  except Exception as error:
    print("MAIL ERROR:", str(error))
    return False
