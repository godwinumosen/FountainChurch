from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import FountainChurchMainPost,FountainChurchMainHeadImage,FountainChurchMinisterHome
#from .models import
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
    
# About page of  the fountain church webapp
def AboutView (request):
    return render(request, 'fountainchurch/about_us.html', {})

# The Contact view been implemented
def ContactView (request):
    email='fountain@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message'] 
        messages.success(request, f'Your email was Successfully sent to Deus Magnus {message_name}..!')
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