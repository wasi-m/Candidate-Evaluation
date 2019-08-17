
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	is_staff = models.BooleanField(default=True)
	pass

	def __str__(self):
		return self.email