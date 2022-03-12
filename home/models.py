from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False, blank=False)
    email=models.EmailField(max_length=50,null=False, blank=False)
    message=models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f'Message from {self.name}'