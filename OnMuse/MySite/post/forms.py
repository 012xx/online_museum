from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'content',
            'tag',
        )

        '''
        djangoでも下の様に表示設定が出来るから必要な時は言って

            widgets = {
                'content': forms.Textarea(
                    attrs={'rows': 10, 'cols': 30, 'placeholder': 'ここに入力'}
                ),
        }
        '''