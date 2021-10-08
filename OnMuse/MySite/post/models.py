from django.db import models
import uuid

class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)
    id = models.UUIDField(verbose_name='タグID',primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(verbose_name='作者',max_length=100,null=False,default="admin")
    title = models.CharField(verbose_name='タイトル',max_length=20,blank=False,null=False)
    content = models.CharField(verbose_name='本文',max_length=140,blank=False,null=False)
    tag = models.ManyToManyField(Tag, verbose_name='タグ',blank=True)#Tagモデルと紐づけ
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True)#Postモデルと紐づけ
    #previews = 見られた回数(展示会を個々で見れるようになってから実装)
    created_at = models.DateTimeField(verbose_name='投稿時間',auto_now_add=True,null=False)
    id = models.UUIDField(verbose_name='作品ID',primary_key=True, default=uuid.uuid4, editable=False,null=False)
    #comments = いつか実装
    #stamp = いつか実装 

    '''
    blankは入力フォーム(入力しないと進めない)
    nullはデータベース(入力しなくても進める)
    idは主キー
    '''
    
    def __str__(self):
        return(self.id)

class Image(models.Model):
    image = models.ImageField(verbose_name='画像',upload_to='images',blank=False,null=False,default = 'images/icon.png')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.CharField(verbose_name='作者',max_length=100,null=False,default="admin")
    comment = models.CharField(verbose_name='コメント',max_length=200,blank=False,null=False)
    postid = models.UUIDField(verbose_name='作品ID',null=False)
    created_at = models.DateTimeField(verbose_name='投稿時間',auto_now_add=True,null=False)

    def __str__(self):
        return self.comment