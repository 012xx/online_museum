from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import Post,Tag,Image
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
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
            return redirect('post:post_list')
    else:#GETの時
        tags = Tag.objects.all()
        posts = Post.objects.all()
        images = Image.objects.all()
        context = {
            'user':request.user,
            "tags":tags,
            "posts":posts,
            "images":images,
        }
    return render(request, 'post/post_create.html', context)

@login_required
def post_list(request):
    context = {
        'post_list': Post.objects.all(),
        'tag': Tag.objects.all(),
        'images':Image.objects.all(),
    }
    return render(request, 'post/post_list.html', context)

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
            return redirect('post:post_list')
    else:#GETの時
        tags = Tag.objects.all()
        posts = Post.objects.all()
        images = Image.objects.all()
        context = {
            'user':request.user,
            "tags":tags,
            "posts":posts,
            "images":images,
        }
    return render(request, 'post/open.html', context)

@login_required
def ranking(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/ranking.html', context)

@login_required
def retail(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/retail.html', context)

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
