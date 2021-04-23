from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Levels(models.Model):
    level_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.level_name)

class Role(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='role')
    role_level = models.OneToOneField(to=Levels, on_delete=models.CASCADE, related_name='role_level')

    def __str__(self):
        return str(self.role_level.level_name)
