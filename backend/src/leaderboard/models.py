from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserEntry(AbstractUser):     #user entry model and field decleration
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):             #user textual representation function
        return f'{self.username}: {self.score}'