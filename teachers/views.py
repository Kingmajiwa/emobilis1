from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to embilis")

def about(request):
    return HttpResponse("About embilis")

def contact(request):
    return HttpResponse("Contact us")

def services(request):
    return HttpResponse("Our services")

def custom_page(request):
    return HttpResponse("This is a custom page")

