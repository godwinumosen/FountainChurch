from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


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


class FountainChurchMinisterHome(models.Model):
    fountain_church_minister_home_title = models.CharField(max_length=255, blank=True, null=True)
    fountain_church_minister_home_position = models.CharField(max_length=255, blank=True, null=True)
    fountain_church_minister_home_description = models.TextField()
    fountain_church_minister_home_img = models.ImageField(upload_to='testy_img/')
    fountain_church_minister_home_author = models.ForeignKey(User, on_delete=models.CASCADE)
    fountain_church_minister_home_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-fountain_church_minister_home_date']
    
    def __str__(self):
        return self.fountain_church_minister_home_title + ' | ' + str(self.fountain_church_minister_home_author)
    
    def get_absolute_url(self):
        return reverse('home',)
    
#THE FOUNTAIN CHURCH EVENT
class ChurchEvent(models.Model):
    Events_title = models.CharField(max_length=255, blank=True, null=True)
    Events_time = models.CharField(max_length=255, blank=True, null=True)
    Events_date_event = models.CharField(max_length=255, blank=True, null=True)
    Events_description = models.TextField()
    Events_slug = models.SlugField(max_length=255, blank=True, null=True)
    Events_img = models.ImageField(upload_to='events_img/')
    Events_author = models.ForeignKey(User, on_delete=models.CASCADE)
    Events_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-Events_date']
    
    def __str__(self):
        return self.Events_title + ' | ' + str(self.Events_author)
    
    def get_absolute_url(self):
        return reverse('home',)
   
#THE FOUNTAIN CHURCH Blog post
class ChurchBlog(models.Model):
    blog_title = models.CharField(max_length=255, blank=True, null=True)
    blog_description = models.TextField()
    blog_slug = models.SlugField(max_length=255, blank=True, null=True)
    blog_img = models.ImageField(upload_to='blog_img/')
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-blog_date']
    
    def __str__(self):
        return self.blog_title + ' | ' + str(self.blog_author)
    
    def get_absolute_url(self):
        return reverse('home',)
    

# The sermons model for fountain church category
class ChurchVideoSermons(models.Model):
    sermons_title = models.CharField(max_length=255, blank=True, null=True)
    Sermons_time = models.CharField(max_length=255, blank=True, null=True)
    sermons_description = models.TextField()
    sermons_preach_by = models.CharField(max_length=100, blank=True, null=True)
    sermons_slug = models.SlugField (max_length=255,blank=True, null=True)
    sermons_video = models.FileField(upload_to='videos/') 
    sermons_youtube_video_link = models.TextField()
    sermons_publish_date = models.DateTimeField (auto_now_add= True)
    sermons_author = models.ForeignKey(User, on_delete=models.CASCADE)
       
    class Meta:
        ordering =['-sermons_publish_date']
    
    def __str__(self):
        return self.sermons_title + ' | ' + str(self.sermons_author)
    
    def get_absolute_url(self):
        return reverse('home')

# The church galary of fountain church
class ChurchGalary(models.Model):
    galary_title = models.CharField(max_length=255, blank=True, null=True)
    galary_img = models.ImageField(upload_to='galary_img/')
    galary_author = models.ForeignKey(User, on_delete=models.CASCADE)
    galary_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-galary_date']
    
    def __str__(self):
        return self.galary_title + ' | ' + str(self.galary_author)
    
    def get_absolute_url(self):
        return reverse('home',)

# The Pastor page of fountain church
class Pastors (models.Model):
    pastor_name = models.CharField(max_length=255, blank=True, null=True)
    pastor_position = models.CharField(max_length=100, blank=True, null=True)
    pastor_img = models.ImageField(upload_to='pass_img/')
    pastor_author = models.ForeignKey(User, on_delete=models.CASCADE)
    pastor_date = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering =['-pastor_date']
    
    def __str__(self):
        return self.pastor_name + ' | ' + str(self.pastor_author)
    
    def get_absolute_url(self):
        return reverse('home',)

class Contactvideo(models.Model):
    contact_video = models.FileField(upload_to='contact_videos/')               



