from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def home(request):
    user = str(request.user)
    if user != "AnonymousUser":
        return redirect('../account/logout')
    else:
        return render(request,'home/index.html')

@login_required
def choice(request):
    context = {
        'user':request.user
    }
    return render(request,'home/choice.html',context)