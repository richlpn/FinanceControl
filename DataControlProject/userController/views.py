from django.shortcuts import render, redirect
from .forms import UserLogin_forms, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_request(request, *args, **kargs):
    context = {
        'form': UserLogin_forms(request.GET),
        'Operation': 'Login'}
    if request.method == "POST":
        context['form'] = UserLogin_forms(request.POST)
        if context['form'].is_valid():

            username = request.POST.get('username')

            password = request.POST.get('password')

            user = authenticate(request, usernme=username, password=password)

            if user is not None:

                login(request, user)

                return redirect("menu/")

    return render(request, "login.html", context)


def logout_view(request, *args, **kargs):
    logout(request)

    return redirect("/menu/")


def createUser_view(request, *args, **kargs):
    context = {
        'form': UserCreationForm(),

        'Operation': 'Registrar'}

    if request.method == 'POST':

        context['form'] = UserCreationForm(request.POST)

        if context['form'].is_valid():

            context['form'].save()

            return redirect('menu/')

    return render(request, 'login.html', context)
