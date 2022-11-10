from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse

class Timestampedmodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(Timestampedmodel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_post_set',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=False, null=True)
    location = models.CharField(max_length=100)

    EXERCISE_TYPE = (
        ('S', '축구'),
        ('B', '농구'),
        ('W', '걷기'),
    )
    exercise = models.CharField(max_length=10, choices=EXERCISE_TYPE)


    def get_absolute_url(self):
        return reverse("sporty:post_detail", args=[self.pk])