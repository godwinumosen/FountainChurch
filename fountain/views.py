from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import FountainChurchMainPost,FountainChurchMainHeadImage,FountainChurchMinisterHome
from .models import ChurchEvent, ChurchBlog, ChurchVideoSermons,ChurchGalary,Pastors,Contactvideo
from .models import ChurchAudioSermons
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
# Create your views here.

'''def HomeView (request):
    return render (request, 'fountainchurch/home.html' )'''
def base (request):
    return render(request,"base.html")

#The main Techbeatrice HomeView page
class HomeView(ListView): 
    model = FountainChurchMainPost
    template_name = 'fountainchurch/home.html'
    
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
    #the first fountain home images
        context['first_images'] = FountainChurchMainHeadImage.objects.all() 
        #the minister home images testimony
        context['testimony_images'] = FountainChurchMinisterHome.objects.all()
        return context 

 #The first fountain ArticleDetailView page
class ArticleDetailView(DetailView):
    model = FountainChurchMainPost
    template_name = 'fountainchurch/article_detail.html'
    def ArticleDetailView(request, pk): 
        object = get_object_or_404(FountainChurchMainPost, pk=pk)
        return render(request, 'fountainchurch/article_detail.html', {'detail': object})   
    
# About page of  the fountain church webapp
def AboutView (request):
    return render(request, 'fountainchurch/about_us.html', {})

# The Contact view been implemented
class ContactView(ListView):
    model = Contactvideo
    template_name = 'fountainchurch/contact.html'

    def get(self, request):
        videos = Contactvideo.objects.all()
        return render(request, self.template_name, {'object_list': videos,})
    def ContactView (request):
        email='fountain@gmail.com'
        if request.method == 'POST':
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']
            message_subject = request.POST['message-subject']
            message = request.POST['message'] 
            messages.success(request, f'Your email was Successfully sent to Church admin {message_name}..!')
            return redirect('/message')
        else:
            context={
                'email':email
            } 
            return render(request, 'fountainchurch/contact.html', {})
        
def message (request):
    return render (request, 'fountainchurch/message.html', {})

#This category is for the Whatsapp API for fountain_whatsapp_number
def fountain_whatsapp_message(request):
    fountain_whatsapp_number = '+2340123456'
    fountain_whatsapp_link = f'https://api.whatsapp.com/send?phone={fountain_whatsapp_number}'
    context = {'whatsapp_link': fountain_whatsapp_link}
    return render(request, 'fountain_whatsapp_message.html', context)

#The main Fountain church Event and news page
class EventsView(ListView): 
    model = ChurchEvent
    template_name = 'fountainchurch/events.html'

#The event of fountain church' article details class base view
class EventBlogArticleDetailView(DetailView):
    model = ChurchEvent
    template_name = 'fountainchurch/event_article.html'
    def DeusMagnusEventBlogArticleDetailView(request, pk): 
        object = get_object_or_404(ChurchEvent, pk=pk)
        return render(request, 'deus_magnus/deus_magnus_event_article.html',{'events_article_detail': object})

#The main Fountain church Event and news page
class BlogView(ListView): 
    model = ChurchBlog
    template_name = 'fountainchurch/blog.html'

#The blog article of the blog project for fountain churc
class BlogArticleDetail(DetailView):
    model = ChurchBlog 
    template_name = 'fountainchurch/blog_article_detail.html'

    def BlogArticleDetail(request, pk):  
        object = get_object_or_404(ChurchBlog, pk=pk)
        return render(request, 'fountainchurch/blog_article_detail.html', {'blog_detail': object})


#The main Fountain church video sermons page
class SermonsView(ListView): 
    model = ChurchVideoSermons
    template_name = 'fountainchurch/sermons.html'

#The sermons article of the blog project for fountain church
class SermonsArticleDetail(DetailView):
    model = ChurchVideoSermons 
    template_name = 'fountainchurch/sermons_article_detail.html'

    def SermonsArticleDetail(request, pk):  
        object = get_object_or_404(ChurchVideoSermons, pk=pk)
        return render(request, 'fountainchurch/sermons_article_detail.html', {'sermons_detail': object})

#The main Fountain church sermons Audio page
class SermonsAudioView(ListView): 
    model = ChurchAudioSermons
    template_name = 'fountainchurch/audio_sermons.html'
    
#The AUDIO sermons article of the blog project for fountain church
class AudioSermonsArticleDetail(DetailView):
    model = ChurchAudioSermons 
    template_name = 'fountainchurch/audio_article_detail.html'

    def AudioSermonsArticleDetail(request, pk):  
        object = get_object_or_404(ChurchAudioSermons, pk=pk)
        return render(request, 'fountainchurch/audio_article_detail.html', {'audio_sermons_detail': object})
    
#The main Fountain church sermons page
class GalaryView(ListView): 
    model = ChurchGalary
    template_name = 'fountainchurch/galary.html'

#The blog article of the blog project for fountain church
class GalaryArticleDetail(DetailView):
    model = ChurchGalary 
    template_name = 'fountainchurch/galary_article_detail.html'

    def GalaryArticleDetail(request, pk):  
        object = get_object_or_404(ChurchGalary, pk=pk)
        return render(request, 'fountainchurch/galary_article_detail.html', {'galary_detail': object})
    

#The pastor view Fountain church page
class PastorsView(ListView): 
    model = Pastors
    template_name = 'fountainchurch/pastors.html'
    
def vision (request):
    return render (request, 'fountainchurch/vision.html', {})