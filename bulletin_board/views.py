from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
sum_=0
def home(request):
    blogs=Blog.objects
    return render(request,"home.html",{"blogs":blogs})

def more(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,"more.html",{"detail":blog_detail})

def new(request):#new.html페이지를 단순히 띄어주는 함수
    return render(request,"new.html")

def create(request,state):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog=Blog()
    blog.pub_date=timezone.datetime.now()
    if state=="page_for_wordcount":
        global sum_
        sum_+=1
        blog.body=request.GET["fulltext"]
        blog.title=str(sum_)
        blog.save() 
        return
    elif state=="page_for_write":
            blog.body=request.GET['body']
            blog.title=request.GET['title']
    blog.save()       
    return redirect('/blog/' + str(blog.id))
