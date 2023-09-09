from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main-page-net'),
    path('profile/<slug:username>/', profile_page, name='profile-page-net'),
    path('register/', register_page, name='register-page-net'),
    path('suggestion/', suggestion_page, name='suggestion-page-net'),
    path('suggestion-watch/', suggestion_watch_page, name='suggestion-watch-page-net'),
]