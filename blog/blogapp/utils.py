from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading

class SendEmailThread(threading.Thread):
  def __init__(self, email):
    self.email = email
    threading.Thread.__init__(self)

  def run(self):
    self.email.send()

def send_reset_password_email(recipient_email, reset_url):
  subject = "Reset Your Password On Djangoblog"
  from_email = 'stha.surja123@gmil.com'
  to_email = [recipient_email]

  html_content = render_to_string('blogapp/password_reset_email.html',{'reset_url': reset_url})

  text_content = strip_tags(html_content)
  email = EmailMultiAlternatives(subject, text_content , from_email, to_email)
  email.attach_alternative(html_content, "text/html")
  SendEmailThread(email).start()