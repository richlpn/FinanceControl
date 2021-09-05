from django.shortcuts import render
from .forms import UserLogin_forms, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_request(request, *args, **kargs):
    context = {
        'form': UserLogin_forms(request.POST or None),
    }
    if request.method == "POST":
        if context['form'].is_valid():

            username = context['form'].cleaned_data.get('username')

            password = context['form'].cleaned_data.get('password')

            user = authenticate(request, usernme=username, password=password)

            if user is not None:

                login(request, user)

                return render(request, "mainController.html", {})

    return render(request, "login.html", context)


def logout_view(request, *args, **kargs):
    logout()

    return render(request, "mainController.html", {})


def createUser_view(request, *args, **kargs):
    context = {'form': UserCreationForm()}
    if request.method == 'POST':
        context['form'] = UserCreationForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()

    return render(request, 'login.html', context)
