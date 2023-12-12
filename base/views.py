from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
# Create your views here.
context = {'year': datetime.now().year}
def home(request):
    return render(request,"home.html",context)
    # return HttpResponse("This is home page")
def about(request):
    return render(request,"about.html",context)
    # return HttpResponse("This is about page")
def projects(request):
    return render(request,"projects.html",context)
    # return HttpResponse("This is projects page")
def contact(request):
    return render(request,"contact.html",context)
    # return HttpResponse("This is contact page")