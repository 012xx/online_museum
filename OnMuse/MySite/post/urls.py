from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('open',views.open,name = 'open'),
    path('ranking',views.ranking,name = 'ranking'),
    path('detail/<uuid:id>',views.detail,name = 'detail'),
    path('search',views.search,name = 'search'),
    path('draw',views.draw,name = 'draw'),
    path('last/<uuid:id>',views.last,name = 'last'),
    path('newranking',views.newranking,name ='newranking')
]