from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,EventsView,EventBlogArticleDetailView,PastorsView
from .views import SermonsView,SermonsArticleDetail,GalaryView,GalaryArticleDetail,ContactView
from .views import SermonsAudioView,AudioSermonsArticleDetail
urlpatterns = [
    #path('', views.HomeView, name='home'),
    #path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('about/', views.AboutView, name='about'),
    #path('contact/', views.ContactView, name='contact'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('message/', views.message, name='message'),
    path('vision/', views.vision, name='vision'),
    path('events/', EventsView.as_view(), name="events"),
    path('events_article_detail/<int:pk>/', EventBlogArticleDetailView.as_view(), name='events_article_detail'),
    path('galary/', GalaryView.as_view(), name='galary'),
    path('galary_article/<int:pk>/', GalaryArticleDetail.as_view(), name="galary_detail"),
    path('sermons/', SermonsView.as_view(), name="sermons"),
    path('sermons_article/<int:pk>/', SermonsArticleDetail.as_view(), name="sermons_detail"),
    path('audio_sermons/', SermonsAudioView.as_view(), name="audio_sermons"),
    path('audio_sermons_detail/<int:pk>/', AudioSermonsArticleDetail.as_view(), name="audio_sermons_detail"),
    path('pastors/', PastorsView.as_view(), name='pastors'),
    
    
]