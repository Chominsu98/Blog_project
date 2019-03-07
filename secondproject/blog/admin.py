from django.contrib import admin
from .models import Blog
# Register your models here.
admin.site.register(Blog)
#실제 admin사이트에서도 클래스에 기입된 내용인 즉 Blog객체를 사용위해서 레지스터 해주는것이다.