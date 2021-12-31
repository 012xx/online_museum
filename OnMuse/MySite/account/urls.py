from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile/<str:id>',views.profile,name='profile'),
    path('profile_change',views.profile_change,name='profile_change'),
]