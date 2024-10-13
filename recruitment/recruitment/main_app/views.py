"""Views for main_app."""
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from recruitment.main_app.forms import UserLoginForm


def main_page(request):
    """View for rendering of main page."""
    context = {
        'title': 'Main',
    }
    return render(request, 'main_app/index.html', context)


@login_required
def to_sith(request):
    """View for transferring to sith page."""
    context = {
        'title': 'Sith Page',
    }
    return render(request, 'main_app/to_sith.html', context)


def login(request):
    """View for rendering of login page."""
    login_form = UserLoginForm()
    if request.method == 'POST':
        data = request.POST
        login_form = UserLoginForm(data=data, files=request.FILES)
        if login_form.is_valid():
            user = auth.authenticate(
                username=data.get('username'),
                password=data.get('password'),
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))
    context = {
        'title': 'Login',
        'login_form': login_form,
    }
    return render(request, 'main_app/login.html', context)


@login_required
def logout(request):
    """View for logging out."""
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))
