from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'home/index.html', {'title': 'Home'})

def courses(request):
    return render(request, 'home/courses.html', {'title': 'Courses'})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

class ContactView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Contact
    fields = ['title', 'feedback']
    success_message = "Your response was successfully submitted!"
    extra_context = {'title': 'Contact Us'}
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)