from django.contrib import admin
from .models import Contact, ContactVerified
# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactVerified)