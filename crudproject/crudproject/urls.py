"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blog.views import index, create_page, create, detail, update, delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('create_page/', create_page, name='create_page' ),
    path('create/', create, name='create' ),
    path('detail/<int:post_id>', detail, name='detail' ),
    path('update/<int:post_id>', update, name='update' ),
    path('delete/<int:post_id>', delete, name='delete' )
]
