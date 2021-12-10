from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime

def home(request):
    user = str(request.user)
    if user != "AnonymousUser":
        return redirect('../account/logout')
    else:
        return render(request,'home/index.html')

@login_required
def choice(request):
    hour = datetime.datetime.now().hour
    if hour < 6:
        msg = "こんばんは"
    elif hour < 10:
        msg = "おはようございます"
    elif hour < 18:
        msg = "こんにちは"
    else:
        msg = "こんばんは"
        
    context = {
        'user':request.user,
        'msg':msg
    }
    return render(request,'home/choice.html',context)