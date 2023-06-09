from os import environ
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Login, User
# Create your views here.
def get_curr_user():
    user = Login.objects.all().values()
    curr_user = ""
    if user:
        curr_user = user[0]['curr_user']
    return curr_user

def index(request):
    curr_user = get_curr_user()
    return render(request,"home.html",{"username":curr_user})
def timetable(request):
    curr_user = get_curr_user()
    return render(request,"timetable.html",{"username":curr_user})
def contact(request):
    curr_user = get_curr_user()
    return render(request,"contact-us.html",{"username":curr_user})
def notes(request):
    curr_user = get_curr_user()
    return render(request,"notes.html",{"username":curr_user})
def divisionlist(request):
    curr_user = get_curr_user()
    return render(request,"division-list.html",{"username":curr_user})
def userlist(request):
    curr_user = get_curr_user()
    users = User.objects.all().values()
    return render(request,"userlist.html",{"username":curr_user,"userlist":users})
def signup(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        prn = request.POST['prn']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        about = request.POST['about']
        age = request.POST['age']

        user = User(fname=fname,lname=lname,prn=prn,email=email,username=username,password=password,about=about,age=age)
        user.save()
        if Login.objects.all():
            curr_user = Login.objects.get(id=1)
            curr_user.curr_user = username
            curr_user.save()
        else:
            curr_user = Login(curr_user=username)
            curr_user.save()
        
        return HttpResponseRedirect('home')

    return render(request,"sign-up.html",{})
    
def login(request):
    user = User.objects.all().values()
    if request.method=="POST":
        for x in user:
            if x["username"]==request.POST['username']:
                if x["password"]==request.POST['password']:
                    if Login.objects.all():
                        curr_user = Login.objects.get(id=1)
                        curr_user.curr_user = x['username']
                        curr_user.save()
                    else:
                        curr_user = Login(curr_user=x['username'])
                        curr_user.save()
                    return HttpResponseRedirect('home')
    return render(request,"login.html",{})
def logout(request):
    curr_user = Login.objects.get(id=1)
    curr_user.curr_user = ""
    curr_user.save()
    return HttpResponseRedirect('home')


def delete(request, id):
  user = User.objects.get(id=id)
  user.delete()
  return HttpResponseRedirect('/userlist')
