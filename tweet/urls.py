from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweetList, name='tweetList'),
    path('create/', views.tweetCreate, name='tweetCreate'),
    path('<int:tweet_id>/edit/', views.tweetEdit, name='tweetEdit'),
    path('<int:tweet_id>/delete/', views.tweetDelete, name='tweetDelete'),
    path('contact/', views.contact, name='contact'),
]
