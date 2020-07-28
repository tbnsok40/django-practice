from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

# Create your views here.


def index(request):
    blog = Blog.objects
    context = dict()
    context['blog'] = blog
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/' + str(blog.id))


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog': blog_detail})
