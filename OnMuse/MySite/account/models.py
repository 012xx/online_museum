from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def icon_path(instance, filename):
    return 'icons/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table    = 'custom_users'
    #名前、ID、自己紹介、リンク、アイコン画像、誕生日、
    introduction = models.TextField(verbose_name='自己紹介',max_length=200,blank=True,null=True,default="よろしくお願いします")
    link = models.URLField(verbose_name='リンク',max_length=200,blank=True,null=True)
    icon = models.ImageField(verbose_name='アイコン画像',upload_to=icon_path,blank=True,null=False,default = '../static/picture/8074e2c65a3ab65d0ce7b482795b7ac0.jpg')
    birthday = models.DateTimeField(verbose_name='生年月日',blank=True,null=True)