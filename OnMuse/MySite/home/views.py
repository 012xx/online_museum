from django.shortcuts import render

def home(request):
    return render(request,'home/index.html',)

def choice(request):
    return render(request,'home/choice.html',)