from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import Post,Tag

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
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
