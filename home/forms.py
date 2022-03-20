from django import forms
from .models import Contact,Newsletter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=['name','email','message']
        
        
        
# newsletter form

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        
# Create user form

class CreationUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control mt-3'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm your password', 'class': 'form-control mt-3 mb-3', }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    