from django.urls import path
from blog.views import index, new, detail, create, create_comment, delete_comment, create_recomment

urlpatterns = [
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<int:blog_id>/', detail, name='detail'),

    path('create_comment/<int:blog_id>', create_comment, name='create_comment'),

    path('delete_comment/<int:com_id>/<int:blog_id>',
         delete_comment, name="delete_comment"),

    path('create_recomment/<int:blog_id>',
         create_recomment, name='create_recomment'),

    # path('delete_recomment/<int:recom_id>/<int:com_id>',
    #      delete_recomment, name="delete_recomment"),

]
