from django.shortcuts import render,HttpResponse
from datetime import datetime
from bertModel.models import Form
from bertModel.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def form(request):
    if request.method=="POST":
        ques=request.POST.get('ques')
        form=Form(ques=ques)
        form.save()

    return render(request,'form.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        uphone=request.POST.get('phone')
        umessage=request.POST.get('message')
        contact= Contact(name=uname,mail=uemail,phone=uphone,message=umessage)
        contact.save()
        messages.success(request, 'Your message has been sent!')
        
    return render(request,'contact.html')

def prediction(request):
    return render(request,'prediction.html')
    