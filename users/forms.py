from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# from django.core.mail import send_mail
# from django.conf import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

    # def send_activation_email(self, msg):
    # 	send_mail(
    # 		'Request for activation',
    # 		msg,
    # 		settings.EMAIL_HOST_USER,
    # 		['evaluate.candidate.head@gmail.com'],
    # 		fail_silently=False,
    # 		)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')