from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField("Is admin",default=False)
    is_user = models.BooleanField("Is User",default=False)

class FileUpload(models.Model):
    file = models.ch
