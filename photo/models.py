from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 1. 모델 : DB 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능, 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면을 보여줄 것이 있다 : 템플릿 작성 (html)

# 외래키 (ForeignKey) - User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키 (PrimaryKey) - User 테이블에 1 admin
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos.no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 모델에 관련된 옵션
    class Meta:
        ordering = ['-updated']  # - : 내림차순 정렬

    # 출력될 내용
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    # 돌아갈 페이지 설정 (success_url : reverse_lazy('돌아갈 URL'))
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])
