from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('open',views.open,name = 'open'),
    path('join/<uuid:id>',views.join,name = 'join'),
    path('ranking/<str:id>',views.ranking,name = 'ranking'),
    path('detail/<uuid:id>',views.detail,name = 'detail'),
    path('like',views.like,name = 'like'),
    path('search',views.search,name = 'search'),
    path('draw',views.draw,name = 'draw'),
    path('last/<uuid:id>',views.last,name = 'last'),
    path('newranking',views.newranking,name ='newranking'),
    path('exhibition',views.exhibition,name = 'exhibition'),
    path('detail-top/<uuid:id>',views.detail_top,name = 'detail-top'),
]