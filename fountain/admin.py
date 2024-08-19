from django.contrib import admin
# Register your models here.
from . import models
from .models import FountainChurchMainPost,FountainChurchMainHeadImage,FountainChurchTestimony



#The Fountain Church Main Admin Post
class FountainChurchMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'fountain_church_slug': ('fountain_church_title',)}
    list_display = ['fountain_church_title','fountain_church_author','fountain_church_img']
admin.site.register(FountainChurchMainPost, FountainChurchMainPostModelAdmin)

class FountainChurchMainHeadImageModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_img_title','fountain_church_img_author','fountain_church_img_img']
admin.site.register(FountainChurchMainHeadImage, FountainChurchMainHeadImageModelAdmin)

class FountainChurchTestimonyModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_testimony_title','fountain_church_testimony_author',
                    'fountain_church_testimony_img']
admin.site.register(FountainChurchTestimony, FountainChurchTestimonyModelAdmin)