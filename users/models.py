from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    WARDEN = 0
    STUDENT = 1

    role = models.SmallIntegerField(null=True)
    block = models.CharField(max_length=5)
    room = models.CharField(max_length=5, null=True)





