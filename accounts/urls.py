from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('blog',views.blog, name='blog'),
    path('posts', views.posts, name='posts'),
    path('logout', views.logout, name='logout')
]
