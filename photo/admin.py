from django.contrib import admin

# Register your models here.
from photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created', 'author__username']
                                         # ForeignKey__ : 해당 모델의 하위키 값 검색
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)