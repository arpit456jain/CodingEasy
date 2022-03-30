from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Message from {self.name}'


# Class for newsletter

class Newsletter(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False)
    subscribe_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email
