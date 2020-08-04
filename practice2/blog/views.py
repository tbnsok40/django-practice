from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import CommentForm, ReCommentForm
from .models import Comment, ReComment
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
    mycom_form = CommentForm()
    myrecom_form = ReCommentForm()
    context = {'comment_form': mycom_form,
               'blog': blog_detail, 'recomment_form': myrecom_form}

    return render(request, 'detail.html', context)


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        temp_form = filled_form.save(commit=False)
        temp_form.post = Blog.objects.get(id=blog_id)
        temp_form.save()

    return redirect('detail', blog_id)


def delete_comment(request, com_id, blog_id):
    mycom = Comment.objects.get(id=com_id)
    mycom.delete()
    return redirect('detail', blog_id)


def create_recomment(request, blog_id):
    filled_form = ReCommentForm(request.POST)
    if filled_form.is_valid():
        filled_form.save()
    return redirect('detail', blog_id)


# def delete_recomment(request, recom_id, com_id):
#     myrecom = ReComment.objects.get(id=com_id)
#     myrecom.delete()
#     return redirect('detail', com_id)
