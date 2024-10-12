"""Views for main_app"""
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from main_app.forms import UserLoginForm


def main_page(request):
    """View for rendering of main page"""
    context = {'title': 'Главная',
               }
    return render(request, 'main_app/index.html', context)


@login_required
def to_sith(request):
    """View for transferring to sith page"""
    context = {'title': 'Переход на страницу для Ситха',
               }
    return render(request, 'main_app/to_sith.html', context)


def login(request):
    """View for rendering of login page"""
    login_form = UserLoginForm()
    if request.method == 'POST':
        data = request.POST
        login_form = UserLoginForm(data=data, files=request.FILES)
        if login_form.is_valid():
            user = auth.authenticate(username=data.get('username'),
                                     password=data.get('password'))
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))
    context = {
        'title': 'Вход',
        'login_form': login_form,
    }
    return render(request, 'main_app/login.html', context)


@login_required
def logout(request):
    """View for logging out"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))
