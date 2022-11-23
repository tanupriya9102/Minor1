from django.shortcuts import render,HttpResponse
from datetime import datetime
from bertModel.models import Form

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
    return render(request,'contact.html')