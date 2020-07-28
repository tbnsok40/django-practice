from django.urls import path
from blog.views import index, new, detail, create

urlpatterns = [
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<int:blog_id>/', detail, name='detail'),

]
