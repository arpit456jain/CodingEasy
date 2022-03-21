from django import forms
from .models import Contact,Newsletter


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
        

    