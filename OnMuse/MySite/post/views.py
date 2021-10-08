from django.shortcuts import render, redirect
from .forms import PostCreateForm,CommentForm
from .models import Comment, Post,Tag,Image
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

@login_required
def open(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post_id = form.save()
            portfolio_images = request.FILES.getlist('image', False)
            for image in portfolio_images:
                image_instance = Image(
                    image = image,
                    post = post_id
                )
                image_instance.save()
            return redirect('post:ranking')
    else:#GETの時
        context = {
            'user':request.user,
            "tags":Tag.objects.all(),
            "posts":Post.objects.all(),
            "images":Image.objects.all(),
        }
    return render(request, 'post/open.html', context)

@login_required
def ranking(request):
    context = {
        'posts': Post.objects.order_by('-created_at'),
        'tags': Tag.objects.all(),
        'images':Image.objects.all(),
    }
    return render(request, 'post/ranking.html', context)

@login_required
def detail(request,id):
    context = {
    'post': Post.objects.filter(id=str(id)).first,
    'tags': Tag.objects.filter(id=str(id)),
    'images':Image.objects.filter(post_id=str(id)),
    }
    return render(request, 'post/detail.html', context)

@login_required
def last(request,id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:last',id=id)
    
    context = {
    'id': id,
    'comments':Comment.objects.filter(postid=str(id)).order_by('-created_at'),
    'user':request.user,
    }
    return render(request, 'post/last.html',context)

@login_required
def search(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/search.html', context)

@login_required
def draw(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/draw.html', context)
