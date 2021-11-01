from django.shortcuts import render, redirect
from .forms import PostCreateForm,CommentForm
from account.models import CustomUser
from .models import Comment, Post,Tag,Image,Like
from django.contrib.auth.decorators import login_required
#from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .flyer_create import flyer1

@login_required
def open(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post_id = form.save()
            portfolio_images = request.FILES.getlist('image', False)
            first = True
            for image in portfolio_images:
                if first:
                    post = Post.objects.filter(id = str(post_id)).first()
                    name = flyer1(image,post.title,post.author)
                    Post.objects.filter(id = str(post_id)).update(flyer = name)
                    first = False
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
        'icons':CustomUser.objects.all(),
        'posts': Post.objects.order_by('-created_at'),
        'tags': Tag.objects.all(),
        'images':Image.objects.all(),
    }
    return render(request, 'post/ranking.html', context)

@login_required
def detail(request,id):
    post = get_object_or_404(Post,id = str(id))
    liked = Like.objects.filter(author = request.user)
    like = ""
    if liked.exists():
        like = post.id
    context = {
    'post': post,
    'tags': Tag.objects.filter(id=str(id)),
    'images': Image.objects.filter(post_id=str(id)),
    'like' : like,
    }
    return render(request, 'post/detail.html', context)

@login_required
def like(request):
    if request.method == "POST":
        post = Post.objects.filter(id = request.POST.get('id'))
        liked = False
        like = Like.objects.filter(author = request.user ,postid = post.id)
        if like.exists():
            like.delete()
        else:
            like.create(author = request.user ,postid = post.id)
            liked = True

        context = {
            'id' : post.id,#article_id
            'liked' : liked,
            'count': post.like.count(),
        }
    
    if request.is_ajax():
        return JsonResponse(context)

@login_required
def last(request,id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:last',id=id)
    
    context = {
    'images':CustomUser.objects.all(),
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

@login_required
def newranking(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/new-ranking.html', context)
