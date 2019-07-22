from django.contrib import admin
from .models import Blog #클래스를 받아온다
# Register your models here.
admin.site.register(Blog)   #register라는 메서드를 쓰는 거겠지?
