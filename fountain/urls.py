from django.urls import path
from . import views
from .views import HomeView #ArticleDetailView

urlpatterns = [
    #path('', views.HomeView, name='home'),
    #path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', views.AboutView, name='about'),
    
]