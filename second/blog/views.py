from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id): #blog_id는 urls.py에 있는 인트형 정수로 표현된 url이다.
    blog_detail = get_object_or_404(Blog, pk = blog_id) #이용자가 원한 몇 번 블로그 객체를 blog_detail에 담는다! , import get_object_or_404 필수

    return render(request, 'detail.html', {'blogs' : blog_detail})