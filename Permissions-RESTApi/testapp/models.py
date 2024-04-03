from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    Choices=[
        ('level1', 'level 1'),
        ('level2', 'level 2'),
        ('level3', 'level 3'),

    ]
    name = models.CharField(max_length=255)
    role = models.CharField(choices=Choices, max_length=20)

    def __str__(self):
        return self.username
    
    def islevel1(self):
        return self.role == 'level1'
    def islevel2(self):
        return self.role == 'level2'
    def islevel3(self):
        return self.role == 'level3'


