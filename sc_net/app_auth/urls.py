from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login-page-net'),
    path('logout/', logout_page, name='logout-page-net')
]