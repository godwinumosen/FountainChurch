from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
'''class Mainvideo(models.Model):
    deus_magnus_first_video = models.FileField(upload_to='main_videos/') '''
# The main model for Deus Magnus Model category
class FountainChurchMainPost(models.Model):
    fountain_church_title = models.CharField(max_length=255, blank=True, null=True)
    fountain_church_description = models.TextField()
    fountain_church_slug = models.SlugField (max_length=255,blank=True, null=True)
    fountain_church_img = models.ImageField(upload_to='images/')
    fountain_church_date = models.DateTimeField (auto_now_add= True)
    fountain_church_author = models.ForeignKey(User, on_delete=models.CASCADE)
       
    class Meta:
        ordering =['-fountain_church_date']
    
    def __str__(self):
        return self.fountain_church_title + ' | ' + str(self.fountain_church_author)
    
    def get_absolute_url(self):
        return reverse('home',)
    
#The head image of the home page
class FountainChurchMainHeadImage(models.Model):
    fountain_church_img_title = models.CharField(max_length=255, blank=True, null=True)
    fountain_church_img_description = models.TextField()
    fountain_church_img_img = models.ImageField(upload_to='img/')
    fountain_church_img_author = models.ForeignKey(User, on_delete=models.CASCADE)
    fountain_church_img_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-fountain_church_img_date']
    
    def __str__(self):
        return self.fountain_church_img_title + ' | ' + str(self.fountain_church_img_author)
    
    def get_absolute_url(self):
        return reverse('home',)


class FountainChurchTestimony(models.Model):
    fountain_church_testimony_title = models.CharField(max_length=255, blank=True, null=True)
    fountain_church_testimony_description = models.TextField()
    fountain_church_testimony_img = models.ImageField(upload_to='testy_img/')
    fountain_church_testimony_author = models.ForeignKey(User, on_delete=models.CASCADE)
    fountain_church_testimony_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-fountain_church_testimony_date']
    
    def __str__(self):
        return self.fountain_church_testimony_title + ' | ' + str(self.fountain_church_testimony_author)
    
    def get_absolute_url(self):
        return reverse('home',)




