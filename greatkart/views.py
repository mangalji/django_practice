from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world, this is the home page of the django.")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("this is the about page of the django.")
    return render('request','about.html')

def contact(request):
    # return HttpResponse("hello, this is a contact page of my website.")
    return render(request,'website/contact.html')