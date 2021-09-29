from django.shortcuts import render
from django.contrib.auth.decorators import login_required

""" def login(request):
    return render(request,'account/login.html',)

def logout(request):
    return render(request,'../home',) """

def signup(request):
    return render(request,'account/signup.html',)

@login_required
def profile(request):
    return render(request,'account/profile.html',)