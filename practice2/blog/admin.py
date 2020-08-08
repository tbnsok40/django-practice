from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)
# recomment는 추가하지 않았는데, 이는 관리자페이지에서 확인하기 위한 용도이기 때문이다.
