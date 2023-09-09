from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from .models import *

def search_profile(requests):
    username = requests.GET.get('search')
    if username:
        return redirect(reverse('profile-page-net', kwargs={'username':username}))
def main_page(requests):
    redirect = search_profile(requests)
    if redirect: return redirect
    return render(requests, 'main-net.html')

def profile_page(requests, username):
    redirect = search_profile(requests)
    if redirect: return redirect

    profile = Person.objects.get(user=User.objects.get(username=username))
    context = {
        'profile':profile,
    }
    return render(requests, 'profile-net.html', context)

def suggestion_page(requests):
    redirect = search_profile(requests)
    if redirect: return redirect

    return render(requests, 'suggestion-net.html')

def suggestion_watch_page(requests):
    redirect = search_profile(requests)
    if redirect: return redirect

    return render(requests, 'suggestion-watch-net.html')

def register_page(requests):
    redirect = search_profile(requests)
    if redirect: return redirect

    if requests.method == 'POST':
        form = CustomUserCreationForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()

        else:
            errors = [error for err in form.errors for error in form.errors[err]]
            form = CustomUserCreationForm()
            context = {
                'error': errors,
                'form': form,
            }
            return render(requests, 'register-net.html', context=context)

    context = {
        'error':None,
        'form':CustomUserCreationForm(),
    }
    return render(requests, 'register-net.html', context=context)