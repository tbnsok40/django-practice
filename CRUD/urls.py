"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from classcrud.views import LetterListView, LetterDetailView, LetterCreateView, LetterDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LetterListView.as_view(), name = 'index'), # as_view() : 클래스도 함수처럼 url에서 바로 보여줄 수 있게 도와주는 메서드
    path('detail/<int:pk>', LetterDetailView.as_view(), name ='detail'), # pk를 detailview에 보내준다.
    path('create/', LetterCreateView.as_view(), name = 'create'),
    path('delete/<int:pk>', LetterDeleteView.as_view(), name = 'delete')
]
