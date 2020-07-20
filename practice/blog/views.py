from django.shortcuts import render, get_object_or_404

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
