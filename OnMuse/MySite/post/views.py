from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import Post,Tag,Image

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST,request.FILES)
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
        form = PostCreateForm()
    return render(request, 'post/post_create.html', {'form': form})

def post_list(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/post_list.html', context)

def open(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post:ranking')
    else:#GETの時
        form = PostCreateForm()
    return render(request, 'post/open.html',{'form': form})

def ranking(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/ranking.html', context)

def retail(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/retail.html', context)

def search(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/search.html', context)
