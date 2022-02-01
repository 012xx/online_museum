from django.contrib import admin

from .models import Post,Tag,Image,Comment,Like,Exhibition

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Exhibition)