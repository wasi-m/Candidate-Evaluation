from django.forms import ModelForm
from .models import Contact, ContactVerified
from users.models import CustomUser
from django import forms

from captcha.fields import CaptchaField

WORKING_CHOICES = (
    (1, ("Yes")),
    (2, ("No"))
)


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'web_address', 'cover_letter', 'like_working']
        cover_letter = forms.CharField(
            max_length=2000,
            help_text='Write here your cover letter!'
        )
        like_working = forms.ChoiceField(choices = WORKING_CHOICES, required=True)
    
    captcha = CaptchaField()

    
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        web_address = cleaned_data.get('web_address')
        cover_letter = cleaned_data.get('cover_letter')
        like_working = cleaned_data.get('like_working')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This Email has already registered.")

        if not name and not email and not cover_letter and not like_working and not web_address:
            raise forms.ValidationError("You have to write something!")


class EvaluationForm(ModelForm):

    class Meta:
        model = ContactVerified
        fields = ['comment', 'review_rating']