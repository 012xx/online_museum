from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm,ProfileChangeForm
from .models import CustomUser
from post.models import Post,Like
from django.shortcuts import get_object_or_404
from django.contrib import messages


""" def login(request):
    return render(request,'account/login.html',)

def logout(request):
    return render(request,'../home',) """

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password = raw_password)
            login(request,user)
            messages.add_message(request, messages.SUCCESS, "アカウント作成完了")
            return redirect('../post/ranking/new')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def profile(request,id):
    user = get_object_or_404(CustomUser,username = id)
    likes = Like.objects.filter(author = id).order_by('created_at')#likes.postidでpostが分かる
    like_list = []
    for like in likes:
        like_list.append(like.postid)
    likes = Post.objects.filter(id__in = like_list)
    context = {
        'user':user,
        'likes':likes,
        'posts': Post.objects.filter(author = user,is_exhibition = False).order_by('-created_at'),
        'exhibitions': Post.objects.filter(author = user,is_exhibition = True).order_by('-created_at'),
    }
    return render(request,'account/profile.html',context)

@login_required
def profile_change(request):
    account = CustomUser.objects.filter(username = request.user).first()
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST,request.FILES,instance = account)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "変更完了")
            return redirect('account:profile',id = request.user)
    context = {
        'account':account,
        'form':ProfileChangeForm()
    }
    return render(request,'account/profile_change.html',context)