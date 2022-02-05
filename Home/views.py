from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    return HttpResponse("<h2 align = 'center'> Hello Home</h2>")

def contact_us(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        email_template_name="contact_info_mail.txt"
        subject='User tried to Contact'

        data={
            "name":name,
            "email":email,
            "message":message
        }
        email = render_to_string(email_template_name, data)
        try:
            send_mail(subject,email,'dbmsprojekt@gmail.com',['codingeasy@gmail.com'],fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/')
    else:
        print('Home')
        return render(request, 'contact/contact.html')
