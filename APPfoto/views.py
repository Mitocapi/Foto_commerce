from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,template_name="APP/base.html")

def first_home_view(request):
    return render(request,template_name="APP/first_home.html")