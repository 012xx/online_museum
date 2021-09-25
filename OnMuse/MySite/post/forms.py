from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'tag',
            'relation'
        )

        '''
        djangoでも下の様に表示設定が出来るから必要な時は言って

            widgets = {
                'content': forms.Textarea(
                    attrs={'rows': 10, 'cols': 30, 'placeholder': 'ここに入力'}
                ),
        }
        '''