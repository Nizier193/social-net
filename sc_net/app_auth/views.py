from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

def search_profile(requests):
    username = requests.GET.get('search')
    if username:
        return redirect(reverse('profile-page-net', kwargs={'username':username}))

def login_page(requests):
    redirect = search_profile(requests)
    if redirect: return redirect

    if requests.method == 'GET':
        if requests.user.is_authenticated:
            return redirect(reverse('profile-page-net', kwargs={'username':requests.user}))
        else:
            return render(requests, 'login-net.html')

    username = requests.POST['username']
    password = requests.POST['password']
    user = authenticate(requests, username=username, password=password)

    if user is not None:
        login(requests, user)
        print(f'{requests.user.username} <--------')
        return redirect(reverse('profile-page-net', kwargs={'username':requests.user}))

    context = {'error':'User wasn`t found.'}
    return render(requests, 'login-net.html', context=context)

def logout_page(requests):
    logout(requests)
    return redirect(reverse('login-page-net'))
