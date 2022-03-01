from django.conf import settings
from django.core.mail import send_mail
import random
from .models import User


def sendOTP(email):
    subject = 'welcome to Hututoo World'
    otp = random.randint(100000, 999999)
    message = f'Hii User\nYour OTP is {otp} for email verification'
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, [email] )
    user = User.objects.get(email = email)
    user.otp = otp
    user.save()
