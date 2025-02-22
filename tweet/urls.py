from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweetPage, name='tweetPage')
]
