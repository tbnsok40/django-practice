from django.db import models

# Create your models here.
class Letter(models.Model): # class는 모델 만들 때 쓴다.
    class Meta: # 클래스 내부의 속성을 정해줄 수 있다.
        verbose_name = '편지'
        # verbose_name_plural = '편지'

    title = models.CharField('제목', max_length=100)
    sender = models.CharField('보낸 이', max_length=100)
    content = models.TextField('편지 내용')

    # 이함수의 이름 마저도 약속이 돼있는 것
    # 클래스 내부에 약속 돼있다.
    def __str__(self):
        return self.title

# makemigrations => migrate : db에 등록한다 모델을. 