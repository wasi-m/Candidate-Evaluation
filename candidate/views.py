from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from captcha.fields import CaptchaField

from .models import Contact
from .forms import ContactForm
from users.models import CustomUser



def register(request):
    if request.method == 'POST' and request.FILES:
        print("in View")
        form = ContactForm(request.POST)

        if form.is_valid():

            human = True
            inputFile = request.FILES['input_Files']
            fs = FileSystemStorage()
            filename = fs.save(inputFile.name, inputFile)
            uploaded_file_url = fs.url(filename)

            new_contact = Contact()
            new_contact.name = form.cleaned_data['name']
            new_contact.email = form.cleaned_data['email']
            new_contact.web_address = form.cleaned_data['web_address']
            new_contact.cover_letter = form.cleaned_data['cover_letter']
            new_contact.like_working = form.cleaned_data['like_working']
            new_contact.file_path = uploaded_file_url

            new_contact.save()
            data = 'success'

            return HttpResponseRedirect('/', {'data':data})

    else:
        form = ContactForm()


    return render(request, 'register.html', {'form': form})
