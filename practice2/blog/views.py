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
        # filled_form.post = Blog.objects.get(id=blog_id)
        # filled_form.save()

        ##############################################################################
        temp_form = filled_form.save(commit=False)  # True하면 왜 에러?

        # 그런데 modelform이 입력받는 값은 body에 대한 값 밖에 없으므로 어떤글에 해당하는 댓글인지 아직 모른다.
        # 그래서 어떤 글인지를 지정해서 저장해야하므로 commit= False옵션을 주고 잠시 저장을 미룬다.
        # 그리고 그 저장을 미룬 상태의 값을 temp_form에 저장했다.

        # 그럼 이걸 위의 코드보다 먼저 선언하면 되는거 아냐? 그럼 굳이 commit=False할 필요도 없고
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
