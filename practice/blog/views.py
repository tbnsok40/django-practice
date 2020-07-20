from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .models import Blog


def index(request):
    blogs = Blog.objects
    context = dict()
    context['blogs'] = blogs
    return render(request, 'index.html', context)


# def detail(request, blog_id):
#     blog_detail = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'detail/detail.html', {'detail': blog_detail})
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def new(request):
    return render(request, 'new.html')


# def create(request):
#     blog = Blog()
#     blog.title = request.GET['title']
#     blog.body = request.GET['body']
#     blog.created_at = timezone.datetime.now()
#     blog.save()
#     return redirect('/blog/'+str(blog.id))
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))
