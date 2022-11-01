# from http.client import HTTPResponse
from datetime import  datetime
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is Homepage")
    context = {
        "variable":"This is sent"
    }
    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')    

def services(request):
    # return HttpResponse("This is Services page") 
    return render(request,'services.html')

def contacts(request):
    # return HttpResponse("This is Contacts Page")
    if request.method == "POST":
       name = request.POST.get('name') 
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       desc = request.POST.get('desc')
       contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today() )
       contact.save()
       messages.success(request, 'Your message has been sent!') 
    return render(request,'contact.html')        