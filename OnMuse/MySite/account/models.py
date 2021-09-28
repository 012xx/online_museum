from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #名前、ID、自己紹介、リンク、アイコン画像、誕生日、
    introduction = models.CharField(verbose_name='自己紹介',max_length=200,blank=True,null=True,default="よろしくお願いします")
    link = models.URLField(verbose_name='リンク',max_length=200,blank=True,null=True)
    icon = models.ImageField(verbose_name='アイコン画像',upload_to='icons',blank=True,null=False,default = 'icons\8074e2c65a3ab65d0ce7b482795b7ac0.jpg')
    birthday = models.DateTimeField(verbose_name='生年月日',blank=True,null=True)