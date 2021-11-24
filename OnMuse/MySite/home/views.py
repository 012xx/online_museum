from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime

def home(request):
    print(request.user.id)
    print(type(request.user))
    user = str(request.user)
    if user != "AnonymousUser":
        return redirect('../account/logout')
    else:
        return render(request,'home/index.html')

@login_required
def choice(request):
    dl = datetime.datetime(year=2021, month=12, day=11, hour=13)
    hour = datetime.datetime.now().hour
    td =  dl - datetime.datetime.now()
    if hour < 6:
        msg = "こんばんは"
    elif hour < 10:
        msg = "おはようございます"
    elif hour < 18:
        msg = "こんにちは"
    else:
        msg = "こんばんは"
    
    msg += "  最終発表まで残り"
    msg += str(td.days)
    msg += "日"
    
    context = {
        'user':request.user,
        'msg':msg
    }
    return render(request,'home/choice.html',context)