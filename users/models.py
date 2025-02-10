from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

class Topic(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    preferred_topics = models.ManyToManyField(Topic, blank=True)
    user_settings = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username}'s profile"
