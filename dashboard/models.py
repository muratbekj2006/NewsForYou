from django.db import models
from users.models import CustomUser
from news.models import Topic, Article
# Create your models here.

class UserDashBoard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prefered_topics = models.ManyToManyField(Topic)
    recently_viewed_articles = models.ManyToManyField(Article)