from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

