from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    list_display = ('username', 'homepage', 'age',)
    fieldsets = UserAdmin.fieldsets + (
        ('Personal Info', {'fields': ('homepage', 'age',)}),
    )

admin.site.register(MyUser, CustomUserAdmin)