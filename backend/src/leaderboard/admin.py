from django.contrib import admin

# Register your models here.
from .models import UserEntry

admin.site.register(UserEntry)