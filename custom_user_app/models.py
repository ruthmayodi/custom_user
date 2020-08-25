from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    

    def __str__(self):
        return self.username

    def get_display_name(self):
        return self.first_name + ' ' + self.last_name