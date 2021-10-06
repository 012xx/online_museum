from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

""" def login(request):
    return render(request,'account/login.html',)

def logout(request):
    return render(request,'../home',) """

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            return redirect('account:login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request,'account/profile.html',)