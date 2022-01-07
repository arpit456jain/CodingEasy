from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return HttpResponse("<h2 align= 'center' > Hello Dashboard</h2>")