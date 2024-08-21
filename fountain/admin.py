from django.contrib import admin
# Register your models here.
from . import models
from .models import FountainChurchMainPost,FountainChurchMainHeadImage,FountainChurchMinisterHome, ChurchEvent



#The Fountain Church Main Admin Post
class FountainChurchMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'fountain_church_slug': ('fountain_church_title',)}
    list_display = ['fountain_church_title','fountain_church_author','fountain_church_img']
admin.site.register(FountainChurchMainPost, FountainChurchMainPostModelAdmin)

class FountainChurchMainHeadImageModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_img_title','fountain_church_img_author','fountain_church_img_img']
admin.site.register(FountainChurchMainHeadImage, FountainChurchMainHeadImageModelAdmin)

class FountainChurchMinisterHomeModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_minister_home_title','fountain_church_minister_home_author',
                    'fountain_church_minister_home_img']
admin.site.register(FountainChurchMinisterHome, FountainChurchMinisterHomeModelAdmin)

class ChurchEventModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'Events_slug': ('Events_title',)}
    list_display = ['Events_title','Events_author','Events_img','Events_description']
admin.site.register(ChurchEvent, ChurchEventModelAdmin)