from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def index(request):
    context = dict()
    all_post = Post.objects.all()
    context['all_post'] = all_post
    
    return render(request, 'index.html', context)
    
def create_page(request):
    return render(request, 'create_page.html')
    
def create(request):
    if request.method == 'POST':
    # 데이터를 한번에 포장하는 것
        Post.objects.create(title=request.POST.get('title'), nickname=request.POST.get('nickname'), body=request.POST.get('body'))
        return redirect('index')
    else:
        return redirect('index')
        
def detail(request, post_id):
    context = dict()
    one_post = Post.objects.get(id=post_id)
    context['one_post'] = one_post
    return render(request,'detail.html', context)
        
    
    # 또 다른 방법, 데이터를 개별로 포장하는 것
    # target_post = Post()
    # target_post.title = request.POST.get('title')
    # target_post.nickname = request.POST.get('nickname')
    # target_post.body = request.POST.get('body')
    # target_post.save()


def update(request, post_id):
    if request.method =='POST':
        update_post = Post.objects.get(id = post_id)
        update_post.title = request.POST.get('title')
        update_post.body = request.POST.get('body')
        update_post.nickname = request.POST.get('nickname')
        update_post.save()
        return redirect('index')
        #update
        # target_post = Post()
        # target_post.title = request.POST.get('title')
        # target_post.nickname = request.POST.get('nickname')
        # target_post.body = request.POST.get('body')
        # target_post.save()
        
        
        
    else:
        
        context = dict()
        one_post = Post.objects.get(id = post_id)
        context['one_post'] = one_post    
        
        return render(request,'create_page.html', context)
        
        
def delete(request, post_id):
    del_post = Post.objects.get(id=post_id)
    del_post.delete()
    return redirect('index')