from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import CustomUser as User_Model

# Create your models here.

WORKING_CHOICES = (
    (1, ("Yes")),
    (2, ("No"))
)

RATING_CHOICES = (
    (1, ("1 star")),
    (2, ("2 star")),
    (3, ("3 star")),
    (4, ("4 star")),
    (5, ("5 star"))
)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    web_address = models.URLField(max_length=60)
    cover_letter = models.CharField(
        max_length=2000,
        help_text='Write here your message!'
    )
    like_working = models.IntegerField(choices=WORKING_CHOICES, default=1)
    file_path = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

class ContactVerified(models.Model):
	verified_on = models.DateTimeField(auto_now_add=True)
	verified_by = models.ForeignKey(User_Model, on_delete=models.CASCADE, related_name='USER_VERIFIED_ID')
	contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='CONTACT_ID')
	comment = models.CharField(
        max_length=2000,
        help_text='Write here your comment!')
	review_rating = models.IntegerField(choices=RATING_CHOICES, default=1)