from datetime import datetime

from django.utils import timezone

from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField("date_created")
    updated_at = models.DateTimeField("date updated")

    def is_published(self):
        now = timezone.now()
        return now >= self.pub_date
