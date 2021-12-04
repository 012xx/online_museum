from django.db import models
import uuid

def images_path(instance, filename):
    return 'images/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

def flyers_path(instance, filename):
    return 'flyers/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)
    id = models.UUIDField(verbose_name='タグID',primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(verbose_name='作者',max_length=100,null=False,default="admin")
    title = models.CharField(verbose_name='タイトル',max_length=20,blank=False,null=False)
    content = models.TextField(verbose_name='本文',max_length=140,blank=False,null=False)
    tag = models.ManyToManyField(Tag, verbose_name='タグ',blank=True)#Tagモデルと紐づけ
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True)#Postモデルと紐づけ
    created_at = models.DateTimeField(verbose_name='投稿時間',auto_now_add=True,null=False)
    id = models.UUIDField(verbose_name='作品ID',primary_key=True, default=uuid.uuid4, editable=False,null=False)
    flyer = models.ImageField(verbose_name='フライヤー',upload_to=flyers_path,blank=False,null=False,default = '../static/picture/8074e2c65a3ab65d0ce7b482795b7ac0.jpg')
    like = models.IntegerField(default=0) 

    '''
    blankは入力フォーム(入力しないと進めない)
    nullはデータベース(入力しなくても進める)
    idは主キー
    '''
    
    def __str__(self):
        return str(self.id)

class Exhibition(models.Model):
    author = models.CharField(verbose_name='作者',max_length=100,null=False,default="admin")
    created_at = models.DateTimeField(verbose_name='投稿時間',auto_now_add=True,null=False)
    id = models.UUIDField(verbose_name='作品ID',primary_key=True, default=uuid.uuid4, editable=False,null=False)
    image = models.ImageField(verbose_name='画像',upload_to=images_path,blank=False,null=False,default = '../static/picture/8074e2c65a3ab65d0ce7b482795b7ac0.jpg')
    like = models.IntegerField(default=0)
    post_id = models.CharField(verbose_name='親ID',max_length=10,null=False,default="admin")
    
    def __str__(self):
        return str(self.id)

class Image(models.Model):
    image = models.ImageField(verbose_name='画像',upload_to=images_path,blank=False,null=False,default = '../static/picture/8074e2c65a3ab65d0ce7b482795b7ac0.jpg')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    author = models.CharField(verbose_name='作者',max_length=100,null=False,default="admin")
    comment = models.TextField(verbose_name='コメント',max_length=100,blank=False,null=False)
    postid = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='投稿時間',auto_now_add=True,null=False)

    def __str__(self):
        return self.comment

class Like(models.Model):
    author = models.CharField(verbose_name='いいねした人',max_length=100,null=False,default="admin")
    postid = models.UUIDField(verbose_name='作品ID',null=False)
    created_at = models.DateTimeField(verbose_name='いいねした時間',auto_now_add=True,null=False)

    def __str__(self):
        return self.postid