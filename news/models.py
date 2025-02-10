from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from users.models import CustomUser
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    url = models.URLField()
    author = models.CharField(max_length=30)
    published_at = models.DateTimeField()
    source = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class UserArticleInteraction(models.Model):
    INTERACTION_TYPE = [
        ('like', 'Like'),
        ('save', 'Save'),
        ('comment', 'Comment'),
        ('share', 'Share'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPE)
    timestamp = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"{self.user} {self.get_interaction_type_display()}ed {self.article.title}"