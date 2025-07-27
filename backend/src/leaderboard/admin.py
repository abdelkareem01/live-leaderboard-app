from django.contrib import admin

# Register your models here.
from .models import UserEntry
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(UserEntry)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Game Data", {"fields": ("score",)}),
    )