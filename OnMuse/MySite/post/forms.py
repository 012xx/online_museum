from django import forms
from django.forms import fields
from .models import Comment, Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'content',
            'tag',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
            'postid',
        )
