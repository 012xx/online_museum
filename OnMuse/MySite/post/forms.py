from django import forms
from django.forms import fields
from .models import Comment, Post,Exhibition

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
            'author',
            'comment',
            'postid',
        )

class ExhibitionCreateForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = (
            'author',
            'image',
            'post_id',
        )