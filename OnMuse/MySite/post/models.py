from django.db import models
import uuid

class Post(models.Model):
    TAG = [
        ('kawaii','かわいい'),
        ('cool','かっこいい'),
    ]
    #user = 製作者名(ログイン後に実装)
    title = models.CharField(max_length=20,blank=False,null=False)
    content = models.CharField(max_length=140,blank=False,null=False)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    category = models.CharField(max_length=30, choices=TAG,blank=True,null=True)
    #previews = 見られた回数(展示会を個々で見れるようになってから実装)
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,null=False)
    #comments = いつか実装
    #stamp = いつか実装 

    '''
    blankは入力フォーム(入力しないと進めない)
    nullはデータベース(入力しなくても進める)
    idは主キー
    '''
    
    def __str__(self):
        return self.title
