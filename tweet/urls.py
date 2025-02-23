from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.tweetList, name='tweetList'),
    path('create/', views.tweetCreate, name='tweetCreate'),
    path('<int:tweet_id>/edit/', views.tweetEdit, name='tweetEdit'),
    path('<int:tweet_id>/delete/', views.tweetDelete, name='tweetDelete'),
    path('contact/', views.contact, name='contact'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout')
]
