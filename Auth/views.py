from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def auth(request):
    return HttpResponse("<h2 align= 'center' > Hello Auth</h2>")