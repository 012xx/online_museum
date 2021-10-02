from django.shortcuts import render,redirect

def home(request):
    user = str(request.user)
    if user != "AnonymousUser":
        return redirect('../account/logout')
    else:
        return render(request,'home/index.html')

def choice(request):
    context = {
        'user':request.user
    }
    return render(request,'home/choice.html',context)