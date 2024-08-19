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