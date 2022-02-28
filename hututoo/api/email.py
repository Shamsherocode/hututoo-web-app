from django.conf import settings
from django.core.mail import send_mail


# def sendMail(request):
#     subject = 'welcome to Hututoo World'
#     message = f'Hi {user.username}, thank you for registering in Hututoo.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [user.email, ]
#     send = send_mail( subject, message, email_from, recipient_list )