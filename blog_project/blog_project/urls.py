"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import bulletin_board.views
import portfolio.views
import wordcounter.views

from django.conf import settings#미디어를 위해서 settings.py에 있는 내용을 가져오기 위함
from django.conf.urls.static import static #이건 그냥 외우자!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcounter.views.home,name="mainhome"),
    path('about/',wordcounter.views.about,name="about"),
    path('result/',wordcounter.views.result,name="result"),

    path('blog/',bulletin_board.views.home,name="home"),
    path('blog/<int:blog_id>',bulletin_board.views.more,name="more"),
    path('blog/new/',bulletin_board.views.new,name="new"),
    path('blog/create/<state>',bulletin_board.views.create,name="create"),

    path('portfolio/',portfolio.views.portfolio,name="portfolio"),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#이와 같은 방식으로 미디어가 url을 타고 들어오는 것이다.