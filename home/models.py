from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False, blank=False)
    email=models.EmailField(max_length=50,null=False, blank=False)
    message=models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f'Message from {self.name}'

    
# Class for newsletter 

class Newsletter(models.Model):
    email=models.EmailField(max_length=50,null=False, blank=False)
    subscribe_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        return email