from django.shortcuts import render, redirect
from .forms import PostCreateForm,CommentForm,ExhibitionCreateForm
from account.models import CustomUser
from .models import Comment, Exhibition, Post,Tag,Image,Like
from django.contrib.auth.decorators import login_required
#from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from functools import reduce
from operator import and_
from .flyer_create import flyer

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
                    choice = request.POST["flyer"]
                    post = Post.objects.filter(id = str(post_id)).first()
                    name = flyer(int(choice),image,post.title,post.author)
                    Post.objects.filter(id = str(post_id)).update(flyer = name)
                    first = False
                image_instance = Image(
                    image = image,
                    post = post_id
                )
                image_instance.save()
            return redirect('post:ranking')
    #GETの時
    context = {
        'user':request.user,
        "tags":Tag.objects.all(),
    }
    return render(request, 'post/open.html', context)

@login_required
def join(request,id):
    if request.method == "POST":
        form = ExhibitionCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post:ranking')
    #GETの時
    context = {
        'user':request.user,
        'post_id' : id
    }
    return render(request, 'post/join.html', context)

@login_required
def ranking(request):
    context = {
        'posts': Post.objects.filter(is_exhibition = False).order_by('-created_at'),
    }
    return render(request, 'post/ranking.html', context)

@login_required
def detail(request,id):
    post = get_object_or_404(Post,id = str(id))
    if post.is_exhibition == True:
        images = Exhibition.objects.filter(post_id = post.id).all()
    else:
        images = Image.objects.filter(post_id=str(id))
    liked = Like.objects.filter(author = request.user).first()
    if liked == None:
        liked = False
    else:
        liked =True
    context = {
    'post': post,
    'tags': Tag.objects.filter(id=str(id)),
    'images': images,
    'like' : post.like,
    'liked' : liked
    }
    return render(request, 'post/detail.html', context)

@login_required
def like(request):
    if request.method == "POST":
        post = get_object_or_404(Post,id = request.POST.get('PostId'))
        liked = False
        like = Like.objects.filter(author = request.user ,postid = post.id)
        if like.exists():
            like.delete()
            post.like -= 1
        else:
            like.create(author = request.user ,postid = post.id)
            post.like += 1
            liked = True
        post.save()

    context = {
        'id' : post.id,#article_id
        'liked' : liked,
        'like': post.like,
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
    post = Post.objects.all()
    keyword = request.GET.get('keyword')
    if keyword:
        exclusion_list = set([' ', '　'])
        q_list = ''

        for i in keyword:
            if i in exclusion_list:#空白を無視
                pass
            else:
                q_list += i

        query = reduce(
                    and_, [Q(title__icontains=q) | Q(content__icontains=q) for q in q_list]
                )
        post = post.filter(query)
    context = {
        'posts': post,
    }
    return render(request, 'post/search.html', context)

@login_required
def exhibition(request):
    context = {
        'post': Post.objects.all(),
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/exhibition.html', context)

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
