from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs=Blog.objects #모델로부터 객체목록들을 다 가져오게 된다.이걸 쿼리셋이라고 부름
    return render(request,"home.html",{"blogs":blogs})
    
def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)#이용자가 원하는 몇 번 블로그의 특정객체
    return render(request,"detail.html",{"blog":blog_detail})    