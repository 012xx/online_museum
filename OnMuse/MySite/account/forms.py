from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='オプション',
        label='苗字',
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='オプション',
        label='名前',
    )
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス',
    )
    introduction = forms.CharField(
        max_length=200,
        required=False,
        label='自己紹介',
    )
    link = forms.URLField(
        max_length=200,
        required=False,
        help_text='有効なリンクを入力してください',
        label='Eメールアドレス',
    )
    icon = forms.ImageField(
        required=False,
        label='アイコン'
    )
    birthday = forms.DateTimeField(
        required=False,
        label='生年月日'
    )

    class Meta:
        model = CustomUser
        fields = ('last_name','username','email','password1','password2', )