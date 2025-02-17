from django.contrib import admin
# Register your models here.
from . import models
from .models import FountainChurchMainPost,FountainChurchMainHeadImage,FountainChurchMinisterHome
from .models import ChurchEvent,ChurchVideoSermons,ChurchGalary,Pastors,Contactvideo,ChurchAudioSermons


#The Fountain Church Main Admin Post
class FountainChurchMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'fountain_church_slug': ('fountain_church_title',)}
    list_display = ['fountain_church_title','fountain_church_author','fountain_church_img']
admin.site.register(FountainChurchMainPost, FountainChurchMainPostModelAdmin)

class FountainChurchMainHeadImageModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_img_title','fountain_church_img_author']
admin.site.register(FountainChurchMainHeadImage, FountainChurchMainHeadImageModelAdmin)

class FountainChurchMinisterHomeModelAdmin (admin.ModelAdmin):
    list_display = ['fountain_church_minister_home_title','fountain_church_minister_home_author',
                    'fountain_church_minister_home_img']
admin.site.register(FountainChurchMinisterHome, FountainChurchMinisterHomeModelAdmin)

class ChurchEventModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'Events_slug': ('Events_title',)}
    list_display = ['Events_title','Events_author','Events_img','Events_description']
admin.site.register(ChurchEvent, ChurchEventModelAdmin)


class ChurchVideoSermonsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'sermons_slug': ('sermons_title',)}
    list_display = ['sermons_title','sermons_author','sermons_video','sermons_description']
admin.site.register(ChurchVideoSermons, ChurchVideoSermonsModelAdmin)

class ChurchAudioSermonsModelAdmin (admin.ModelAdmin):
    list_display = ['audio_sermons_title']
admin.site.register(ChurchAudioSermons, ChurchAudioSermonsModelAdmin)
class ChurchGalaryModelAdmin (admin.ModelAdmin):
    list_display = ['galary_title','galary_author','galary_img']
admin.site.register(ChurchGalary, ChurchGalaryModelAdmin)

class PastorsModelAdmin (admin.ModelAdmin):
    list_display = ['pastor_name','pastor_author','pastor_img']
admin.site.register(Pastors, PastorsModelAdmin)

class ContactvideoModelAdmin (admin.ModelAdmin):
    list_display = ['contact_video']
admin.site.register(Contactvideo, ContactvideoModelAdmin)