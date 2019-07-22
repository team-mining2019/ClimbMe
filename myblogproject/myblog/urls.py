from django.contrib import admin
from django.urls import path
#import myblog.views 이것도 되어야하는데 안된다..
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name="newblog"),
]