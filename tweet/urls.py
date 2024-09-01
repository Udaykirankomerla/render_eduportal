# from django.contrib import admin
from django.urls import path

from user.views import signup
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.index, name='index.html'),
    
    path('', views.tweet_list, name='tweet_list'),
    path('signup/', signup, name='signup'),
    path('signin/', signup, name='signin'),    #signup from user app
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
]