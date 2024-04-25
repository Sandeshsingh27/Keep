from django.db import models

# Create your models here.


class Note(models.Model):
    # title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]
    
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]
