from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Contact(models.Model):
    title = models.CharField(max_length=100)
    feedback = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-contact')
