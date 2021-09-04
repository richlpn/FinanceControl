from django.http import request
from django.shortcuts import render

# Create your views here.

def get_all(request: request,*args,**kargs):
    context = {}
    
    if request.method == "POST":
        pass
    elif request.method == "GET":
        context["user"] =request.user

    return render(request,"<h1>Get All<\h1>",context)
