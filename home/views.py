from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from django.contrib import messages
from .forms import ContactForm, CreationUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import Newsletter
from .forms import ContactForm, NewsletterForm


def index(request):
    return render(request, 'home/index.html')


def feature(request):
    return render(request, 'home/Features/features.html')


def pricing(request):
    return render(request, 'home/Pricing/pricing.html')


def editor(request):
    return render(request, 'home/Editor/editor.html')

@unauthenticated_user
def register(request):
    if request.method != 'POST':
        form = CreationUserForm()
        context = {'form': form}
        return render(request, 'home/Login/login.html', context)
    form = CreationUserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_valid = False
        user.save()
    else:
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request, 'Username already exists')
        elif request.POST['password1'] != request.POST['password2']:
            messages.info(request, 'Password not matched')
        else:
            messages.info(request, form.errors)
        form = CreationUserForm()
        context = {'form': form}
        return render(request, 'home/Login/login.html', context)
    messages.success(request, ('Successful'))
    return redirect('login')


@unauthenticated_user
def login(request):  # sourcery skip: hoist-statement-from-if
    if request.method != 'POST':
        form = CreationUserForm()
        context = {'form': form}
        return render(request, 'home/Login/login.html', context)
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'Username of password wrong')
        return redirect('login')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                request, ('There was an error in your form! try again...'))
            return render(request, 'home/contact/contact.html')
        messages.success(
            request, ('Thank you for contacting us'), extra_tags='success')
        return redirect('index')
    return render(request, 'home/contact/contact.html')

# newsletter view


def subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST or None)
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.warning(
                request, ('Sorry! this email is already exist'), extra_tags='warning')
            return redirect('index')
        else:
            instance.save()
            messages.success(
                request, ('Thank you for subscribing to our newsletter'), extra_tags='success')
            return redirect('index')
    return render(request, 'home/index.html')


def html(request):
    return render(request, 'home/Html/html.html')


def html1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, 'home/Html/Basic/Basic.html')
    elif query == "images":
        return render(request, 'home/Html/Images/images.html')
    elif query == "link":
        return render(request, 'home/Html/Links/link.html')
    elif query == "list":
        return render(request, 'home/Html/Lists/list.html')
    elif query == "table":
        return render(request, 'home/Html/Table/table.html')
    elif query == "style":
        return render(request, 'home/Html/Style/style.html')


def css(request):
    return render(request, 'home/css/css.html')


def css1(request):
    query = request.GET.get('data')
    if query == "align":
        return render(request, 'home/css/align/align.html')
    elif query == "basic":
        return render(request, 'home/css/basic/basic.html')
    elif query == "color":
        return render(request, 'home/css/color/color.html')
    elif query == "font-family":
        return render(request, 'home/css/font-family/font-family.html')
    elif query == "font-style":
        return render(request, 'home/css/font-style/font-style.html')
    elif query == "function":
        return render(request, 'home/css/functions/functions.html')
    elif query == "margins":
        return render(request, 'home/css/margins/margins.html')
    elif query == "padding":
        return render(request, 'home/css/padding/padding.html')
    elif query == "selectors":
        return render(request, 'home/css/selectors/selectors.html')


def bootstrap(request):
    return render(request, 'home/bootstrap/bootstrap.html')


def bootstrap1(request):
    query = request.GET.get('data')
    if query == "button":
        return render(request, 'home/bootstrap/button/button.html')
    elif query == "cards":
        return render(request, 'home/bootstrap/cards/cards.html')
    elif query == "carousel":
        return render(request, 'home/bootstrap/carousel/carousel.html')
    elif query == "color":
        return render(request, 'home/bootstrap/color/color.html')
    elif query == "container":
        return render(request, 'home/bootstrap/container/container.html')
    elif query == "grid":
        return render(request, 'home/bootstrap/grid/grid.html')
    elif query == "jumbotron":
        return render(request, 'home/bootstrap/jumbotron/jumbotron.html')
    elif query == "modal":
        return render(request, 'home/bootstrap/modal/modal.html')
    elif query == "navbar":
        return render(request, 'home/bootstrap/navbar/navbar.html')


def js(request):
    return render(request, 'home/javascr/javascr.html')


def js1(request):
    query = request.GET.get('data')
    if query == "datatype":
        return render(request, 'home/javascr/datatypes/datatypes.html')
    elif query == "event":
        return render(request, 'home/javascr/events/events.html')
    elif query == "functions":
        return render(request, 'home/javascr/functions/functions.html')
    elif query == "class":
        return render(request, 'home/javascr/jsclasses/jsclasses.html')
    elif query == "condition":
        return render(request, 'home/javascr/jsconditions/jsconditions.html')
    elif query == "error":
        return render(request, 'home/javascr/jserrors/jserrors.html')
    elif query == "math":
        return render(request, 'home/javascr/jsmath/jsmath.html')
    elif query == "number":
        return render(request, 'home/javascr/jsnumbers/jsnumbers.html')
    elif query == "operator":
        return render(request, 'home/javascr/operators/operators.html')
    elif query == "string":
        return render(request, 'home/javascr/string/string.html')
    elif query == "syntax":
        return render(request, 'home/javascr/syntax/syntax.html')
    elif query == "object":
        return render(request, 'home/javascr/objects/objects.html')


# Add views for jQuery Course
def jQuery(request):
    return render(request, 'home/jQuery/jQuery.html')


def jQuery1(request):
    query = request.GET.get('data')
    if query == "overview":
        return render(request, 'home/jQuery/Overview/Overview.html')
    elif query == "selector":
        return render(request, 'home/jQuery/Overview/selectors.html')
    elif query == "attribute":
        return render(request, 'home/jQuery/Attributes/attributes.html')
    elif query == "manipulatingCSS":
        return render(request, 'home/jQuery/ManipulatingCSS/ManipulatingCSS.html')
    elif query == "jQueryCss":
        return render(request, 'home/jQuery/ManipulatingCSS/jQueryCss.html')
    elif query == "jQueryDimensions":
        return render(request, 'home/jQuery/ManipulatingCSS/jQueryDimensions.html')
    # The complete of jQuery course
    elif query == "manipulatingDOM":
        return render(request, 'home/jQuery/ManipulatingDOM/ManipulatingDOM.html')
    elif query == "events":
        return render(request, 'home/jQuery/Events/events.html')
    elif query == "effects":
        return render(request, 'home/jQuery/Effects/effects.html')


def py(request):
    return render(request, 'home/Python/python.html')


def py1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, 'home/Python/Basic/Basic.html')
    elif query == "condition":
        return render(request, 'home/Python/Conditions/condition.html')
    elif query == "datatype":
        return render(request, 'home/Python/DataTypes/datatypes.html')
    elif query == "file":
        return render(request, 'home/Python/File Handling/file.html')
    elif query == "function":
        return render(request, 'home/Python/Functions/function.html')
    elif query == "loop":
        return render(request, 'home/Python/Loop/loop.html')
    elif query == "operator":
        return render(request, 'home/Python/Operator/operator.html')
    elif query == "regex":
        return render(request, 'home/Python/RegEx/regex.html')


def cpp(request):
    return render(request, 'home/CPP/cpp.html')


def cpp1(request):
    query = request.GET.get('data')
    if query == "constant":
        return render(request, 'home/CPP/Constants/Literals/Constants.html')
    elif query == "datatype":
        return render(request, 'home/CPP/Data_Types/data_types.html')
    elif query == "modifier":
        return render(request, 'home/CPP/Modifiers/modifiers.html')
    elif query == "variable":
        return render(request, 'home/CPP/Variable_Types/Variable_Types.html')
    elif query=="storage":
            return render(request,'home/CPP/Storage_Classes/storage_classes.html')
    elif query=="operators":
            return render(request,'home/CPP/Operators/operators.html')
    elif query=="loops":
            return render(request,'home/CPP/Loops/loops.html')
    


def ml(request):
    return render(request, 'home/ML/ML.html')


def ml1(request):
    query = request.GET.get('data')
    if query == "linregx":
        return render(request, 'home/ML/Linear_Regression/Linear_Regression.html')
    elif query == "logregx":
        return render(request, 'home/ML/Logistic_Regression/Logistical_Regression.html')
    elif query == "knn":
        return render(request, 'home/ML/K_Nearest_Neighbors/K_Nearest_Neighbors.html')
    elif query == "decitree":
        return render(request, 'home/ML/Decision_Tree/Decision_Tree.html')
    elif query == "kmc":
        return render(request, 'home/ML/K_Means_Clustering/K_Means_Clustering.html')
    elif query == "nv":
        return render(request, 'home/ML/Naive_Bayes/Naive_Bayes.html')
    elif query == "rf":
        return render(request, 'home/ML/Random_Forest/Random_Forest.html')
    elif query == "svm":
        return render(request, 'home/ML/Support_Vector_Machines/Support_Vector_Machines.html')
    elif query == "hrc":
        return render(request, 'home/ML/Hierarchical Clustering/Hierarchical Clustering.html')
    elif query == "ohe":
        return render(request, 'home/ML/One Hot Encoding/One Hot Encoding.html')
    elif query == "kcv":
        return render(request, 'home/ML/K-Fold Cross Validation/K-Fold Cross Validation.html')
    elif query == "gs":
        return render(request, 'home/ML/Gridsearch/Gridsearch.html')



def django(request):
    return render(request, 'home/Django/django.html')


def django1(request):
    query = request.GET.get('data')
    if query == "basic":
        return render(request, 'home/Django/Basic/basic.html')
    elif query == "enviroment":
        return render(request, 'home/Django/Enviroment/enviroment.html')
    elif query == "project":
        return render(request, 'home/Django/Project/project.html')
    elif query == "view":
        return render(request, 'home/Django/View/view.html')
    elif query == "url":
        return render(request, 'home/Django/Urls/url.html')
    elif query == "model":
        return render(request, 'home/Django/Model/model.html')
    elif query == "auth":
        return render(request, 'home/Django/Authentication/auth.html')
    elif query == "template":
        return render(request, 'home/Django/Template/template.html')


def course_video(request):
    return render(request, 'home/Course_video/video_page.html')


# Adding views to render courses

# def newcourse(request):
#     return render(request, 'home/newcourse/newcourse.html')


# def newcourse1(request):
#     query = request.GET.get('data')
#     if query == "topic1":
#         return render(request, 'home/newcourse/topic1/topic1.html')
#     elif query == "topic2":
#         return render(request, 'home/newcourse/topic2/topic2.html')
