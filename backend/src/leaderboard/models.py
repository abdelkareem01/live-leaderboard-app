from django.db import models

# Create your models here.

class UserEntry(models.Model):     #user entry model and field decleration
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):             #user textual representation function
        return f'{self.name}: {self.score}'