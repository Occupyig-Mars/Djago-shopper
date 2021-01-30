from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .import forms
from django.http import HttpResponse
from .models import credentails, links 

# Create your views here.


def indexView(request):
     return render(request,'index.html')

'''@login_required
def dashboardView(request):
    return render(request,'dashboard.html')'''


def registerView(request):
     if request.method =="POST":
          form=UserCreationForm(request.POST)
          
                   
          if form.is_valid():
               form.save()
               return redirect('login_url')
     else:
          form=UserCreationForm()
    
     return render(request,'registration/register.html',{'form':form})

def dashboardView(request):
     if request.method == 'POST':
          forme = forms.Creden(request.POST)
          if forme.is_valid():
             forme.save()
             return redirect('accounts:login_url')
               
               
     else:
          forme = forms.Creden()
     return render(request,'dashboard.html',{'forms':forme})


def mainView(request):
  link = request.GET.get("link") # This will get the variable from the form
  size = request.GET.get("size")
  
  my_script(link,size)
  return render(request,'main.html')

def my_script(link,size):
    print(link)
    print(size) 
    cre = credentails.objects.values('cc') #use this as your credit card dettails
    print (cre)
    email = credentails.objects.values('email') #use this as your email
    print (email) 
    address = credentails.objects.values('address') #use this as your address
    print (address)
    phone = credentails.objects.values('phone') #use this as your phone no.
    print (phone)
    zip = credentails.objects.values('zip_code') #use this as your zip code
    print (zip)
    

    #run your script here
