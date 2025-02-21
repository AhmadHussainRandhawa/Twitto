from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_page, name='tweet_page')
]
