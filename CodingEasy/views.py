import imp
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreationUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt


@csrf_exempt
def contact_us(request):
    if request.method == "POST":
        print("IN POST")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_template_name = "contact/contact_info_mail.txt"
        subject = 'User tried to Contact'

        data = {
            "name": name,
            "email": email,
            "message": message
        }
        email = render_to_string(email_template_name, data)
        try:

            send_mail(subject, email, 'dbmsprojekt@gmail.com',
                      ['codingeasy@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponse('Email sent')
    else:
        print('Coding Easy')
        return render(request, 'contact/contact.html')


def index(request):
    return render(request, 'index.html')


def registerPage(request):
    form = CreationUserForm()

    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)

    context = {'form': form}
    return render(request, './login/login.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, './login/login.html', context)


def feature(request):
    return render(request, './Features/features.html')


def pricing(request):
    return render(request, './Pricing/pricing.html')


def html(request):
    return render(request, './html/html.html')


def html1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, './html/basic/basic.html')
    elif query == "images":
        return render(request, './html/Images/images.html')
    elif query == "link":
        return render(request, './html/Links/link.html')
    elif query == "list":
        return render(request, './html/Lists/list.html')
    elif query == "table":
        return render(request, './html/Table/table.html')
    elif query == "style":
        return render(request, './html/Style/style.html')


def css(request):
    return render(request, './css/css.html')


def css1(request):
    query = request.GET.get('data')
    if query == "align":
        return render(request, './css/align/align.html')
    elif query == "basic":
        return render(request, './css/basic/basic.html')
    elif query == "color":
        return render(request, './css/color/color.html')
    elif query == "font-family":
        return render(request, './css/font-family/font-family.html')
    elif query == "font-style":
        return render(request, './css/font-style/font-style.html')
    elif query == "function":
        return render(request, './css/functions/functions.html')
    elif query == "margins":
        return render(request, './css/margins/margins.html')
    elif query == "padding":
        return render(request, './css/padding/padding.html')
    elif query == "selectors":
        return render(request, './css/selectors/selectors.html')


def bootstrap(request):
    return render(request, './bootstrap/bootstrap.html')


def bootstrap1(request):
    query = request.GET.get('data')
    if query == "button":
        return render(request, './bootstrap/button/button.html')
    elif query == "cards":
        return render(request, './bootstrap/cards/cards.html')
    elif query == "carousel":
        return render(request, './bootstrap/carousel/carousel.html')
    elif query == "color":
        return render(request, './bootstrap/color/color.html')
    elif query == "container":
        return render(request, './bootstrap/container/container.html')
    elif query == "grid":
        return render(request, './bootstrap/grid/grid.html')
    elif query == "jumbotron":
        return render(request, './bootstrap/jumbotron/jumbotron.html')
    elif query == "modal":
        return render(request, './bootstrap/modal/modal.html')
    elif query == "navbar":
        return render(request, './bootstrap/navbar/navbar.html')


def js(request):
    return render(request, './javascr/javascr.html')


def js1(request):
    query = request.GET.get('data')
    if query == "datatype":
        return render(request, './javascr/datatypes/datatypes.html')
    elif query == "event":
        return render(request, './javascr/events/events.html')
    elif query == "functions":
        return render(request, './javascr/functions/functions.html')
    elif query == "class":
        return render(request, './javascr/jsclasses/jsclasses.html')
    elif query == "condition":
        return render(request, './javascr/jsconditions/jsconditions.html')
    elif query == "error":
        return render(request, './javascr/jserrors/jserrors.html')
    elif query == "math":
        return render(request, './javascr/jsmath/jsmath.html')
    elif query == "number":
        return render(request, './javascr/jsnumbers/jsnumbers.html')
    elif query == "operator":
        return render(request, './javascr/operators/operators.html')
    elif query == "string":
        return render(request, './javascr/string/string.html')
    elif query == "syntax":
        return render(request, './javascr/syntax/syntax.html')
    elif query == "object":
        return render(request, './javascr/objects/objects.html')


def py(request):
    return render(request, './Python/python.html')


def py1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, './Python/Basic/Basic.html')
    elif query == "condition":
        return render(request, './Python/Conditions/condition.html')
    elif query == "datatype":
        return render(request, './Python/DataTypes/datatypes.html')
    elif query == "file":
        return render(request, './Python/File Handling/file.html')
    elif query == "function":
        return render(request, './Python/Functions/function.html')
    elif query == "loop":
        return render(request, './Python/Loop/loop.html')
    elif query == "operator":
        return render(request, './Python/Operator/operator.html')
    elif query == "regex":
        return render(request, './Python/RegEx/regex.html')


def cpp(request):
    return render(request, './CPP/cpp.html')


def cpp1(request):
    query = request.GET.get('data')
    if query=="constant":
        return render(request,'./CPP/Constants/Literals/Constants.html')
    elif query=="datatype":
        return render(request,'./CPP/Data_Types/data_types.html')
    elif query=="modifier":
        return render(request,'./CPP/Modifiers/modifiers.html')
    elif query=="variable":
        return render(request,'./CPP/Variable_Types/Variable_Types.html')
    elif query=="storage":
        return render(request,'./CPP/Storage_Classes/storage_classes.html')
    elif query=="operators":
        return render(request,'./CPP/Operators/operators.html')
    elif query=="loops":
        return render(request,'./CPP/Loops/loops.html')
    


def ml(request):
    return render(request, './ML/ML.html')


def ml1(request):
    query = request.GET.get('data')
    if query == "linregx":
        return render(request, './ML/Linear_Regression/Linear_Regression.html')
    elif query == "logregx":
        return render(request, './ML/Logistic_Regression/Logistical_Regression.html')
    elif query == "knn":
        return render(request, './ML/K_Nearest_Neighbors/K_Nearest_Neighbors.html')
    elif query == "decitree":
        return render(request, './ML/Decision_Tree/Decision_Tree.html')
    elif query == "kmc":
        return render(request, './ML/K_Means_Clustering/K_Means_Clustering.html')
    elif query == "nv":
        return render(request, './ML/Naive_Bayes/Naive_Bayes.html')
    elif query == "rf":
        return render(request, './ML/Random_Forest/Random_Forest.html')
    elif query == "svm":
        return render(request, './ML/Support_Vector_Machines/Support_Vector_Machines.html')
    elif query == "ohe":
        return render(request, './ML/One Hot Encoding/One Hot Encoding.html')
    elif query == "kcv":
        return render(request, './ML/K-Fold Cross Validation/K-Fold Cross Validation.html')
    elif query == "gs":
        return render(request, './ML/Gridsearch/Gridsearch.html')


def django(request):
    return render(request, './Django/django.html')


def django1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, './Django/Basic/basic.html')
    elif query == "enviroment":
        return render(request, './Django/Enviroment/enviroment.html')
    elif query == "project":
        return render(request, './Django/Project/project.html')
    elif query == "view":
        return render(request, './Django/View/view.html')
    elif query == "url":
        return render(request, './Django/Urls/url.html')
    elif query == "model":
        return render(request, './Django/Model/model.html')
    elif query == "auth":
        return render(request, './Django/Authentication/auth.html')
    elif query == "template":
        return render(request, './Django/Template/template.html')


def course_video(request):
    return render(request, './Course_video/video_page.html')
