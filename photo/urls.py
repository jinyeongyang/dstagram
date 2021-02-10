from django.urls import path

from photo.views import photo_list

app_name = 'photo'  # 2차 url

urlpatterns = [
    path('', photo_list, name='photo_list')
            # 클래스형 뷰에서는 .as_view()가 붙어야함
]
