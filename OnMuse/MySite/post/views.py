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
import re
from django.contrib import messages

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
                    back_color = request.POST["back_color"]
                    character_color = request.POST["character_color"]
                    post = Post.objects.filter(id = str(post_id)).first()
                    name = flyer(int(choice),back_color,character_color,image,post.title,post.author)
                    Post.objects.filter(id = str(post_id)).update(flyer = name)
                    first = False
                image_instance = Image(
                    image = image,
                    post = post_id
                )
                image_instance.save()
            messages.add_message(request, messages.SUCCESS, "投稿完了")
            return redirect('ranking/new')
    #GETの時
    else:
        form = PostCreateForm()
    context = {
        'form':form,
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
            messages.add_message(request, messages.SUCCESS, "投稿完了")
            return redirect('post:detail',id = id)
    #GETの時
    context = {
        'user':request.user,
        'post_id' : id
    }
    return render(request, 'post/join.html', context)

@login_required
def ranking(request,id):
    new = "btn btn-off"
    hot = "btn btn-off"
    week = "btn btn-off"
    month = "btn btn-off"
    if id == "new":
        posts = Post.objects.filter(is_exhibition = False).order_by('-created_at')
        new = "btn btn-on"
    elif id == "hot":
        posts = Post.objects.filter(is_exhibition = False).order_by('-like')
        hot = "btn btn-on"
    elif id == "week":
        posts = Post.objects.filter(is_exhibition = False).order_by('-like')
        week = "btn btn-on"
    else:
        posts = Post.objects.filter(is_exhibition = False).order_by('-like')
        month = "btn btn-on"
    context = {
        'new':new,
        'hot':hot,
        'week':week,
        'month':month,
        'posts': posts,
    }
    return render(request, 'post/ranking.html', context)

@login_required
def detail(request,id):
    post = get_object_or_404(Post,id = str(id))
    post.views += 1
    post.save()
    if post.is_exhibition == True:
        images = Exhibition.objects.filter(post_id = post.id).all()
    else:
        images = Image.objects.filter(post_id=str(id))
    like = Like.objects.filter(author = request.user, postid = post.id)
    if like.exists():
        liked = True
    else:
        liked = False
    context = {
    'post': post,
    'tags': Tag.objects.filter(id=str(id)),
    'images': images,
    'like' : post.like,
    'liked' : liked
    }
    return render(request, 'post/detail.html', context)

@login_required
def detail_top(request,id):
    post = get_object_or_404(Post,id = str(id))
    content1 = post.content[:22]
    content2 = post.content[22:]
    views = str(post.views).zfill(6)
    context = {
        'account' : CustomUser.objects.filter(username = post.author).first(),
        'post': post,
        'content1':content1,
        'content2':content2,
        'views': views,
        'tag': Tag.objects.all(),
    }
    return render(request, 'post/detail-top.html', context)

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
        'post': Post.objects.filter(id = id).first(),
        'user':request.user,
    }
    return render(request, 'post/last.html',context)

@login_required
def search(request):
    post = Post.objects.all()
    keyword = request.GET.get('keyword')
    tag_list = []#list型のタグ
    if keyword:
        keyword.replace("＃","#")
        keyword = re.split('[ 　]',keyword)
        for i in range(len(keyword)):
            if "#" in keyword[i]:
                tag_list.append(keyword[i][1:])
        for i in range(len(tag_list)):
            try:
                keyword.remove("#" + tag_list[i])
            except:#存在しないタグが検索された場合pass
                pass
        keyword = ''.join(keyword)#連結したキーワード
        if keyword:
            query = reduce(
                        and_, [Q(title__icontains=q) | Q(content__icontains=q) for q in keyword]
                    )
            post = post.filter(query)
        post = post.filter(is_exhibition = 0)
        tags = Tag.objects.filter(name__in = tag_list).all()
        for tag in tags:
            post = post.filter(tag = tag.id)
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
