from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os 

BASE_DIR = settings.BASE_DIR
RECEIPT_EMAIL = settings.RECEIPT_EMAIL

def send_email(subject, email_content, files):
    email_message = EmailMessage(
                subject=subject,
                body=email_content,
                from_email='settings.EMAIL_HOST_USER',
                to=[RECEIPT_EMAIL],
            )
    
    if len(files) > 0:
                for f in files:
                    path = f'{BASE_DIR}/{f}'
                    email_message.attach_file(path)
                    os.remove(path)
                    
    email_message.send(fail_silently=False)
    
