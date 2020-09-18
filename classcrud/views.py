from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from classcrud.models import Letter
from django.urls import reverse_lazy
def index(request):
    return render(request, 'index.html')
# Create your views here.
class LetterListView(ListView):
    model = Letter
    ################# 이미 정해진 대로 변수명 사용할거면 아래는 날려도 돼 -> 그만큼 깔끔함 
    # html 이름까지 바꾸게 되는데 (letter_list.html로)
    template_name = 'index.html' # template 네임을 오버라이딩 해준다.
    #html에 보여줄 변수도 오버라이딩 해주자
    context_object_name = 'letters'

class LetterDetailView(DetailView):
    model = Letter
    template_name = 'detail.html' # template 네임을 오버라이딩 해준다.
    context_object_name = 'letter_object'

class LetterCreateView(CreateView):
    model = Letter
    # fields는 무조건 필요하다 (속성상 규정)
    fields = '__all__'
    # fields = ['title','sender','content'] # 모델폼을 이 클래스에서 알아서 생성해준다 굉장히 편해
    template_name = 'create.html'

    success_url = reverse_lazy('index') # reverse_lazy라는 함수에 넣어준다 # url name = 'index'

class LetterDeleteView(DeleteView):
    model = Letter

    # delete가 success되면 index로 보낸다. 그러니까 우선 지워야해서 confirm.html로 가는 것이다.
    success_url = reverse_lazy('index')


    # 삭제 버튼을 누르는 것 자체가 GET방식이기 때문에(누르는 것 자체가 get)
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)