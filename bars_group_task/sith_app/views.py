"""Views for sith_app"""
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sith_app.models import Sith
from sith_app.forms import SithForm
from common import SHADOW_HANDS_MAX_NUMBER
from logs.log_config import LOGGER


def sith_login(request):
    """View for rendering of sith login page"""
    queryset = Sith.get_items()
    label = 'Выберите себя из списка Ситхов'
    login_form = SithForm(queryset=queryset, label=label)
    if request.method == 'POST':
        login_form = SithForm(queryset=queryset, label=label,
                              data=request.POST, files=request.FILES)
        if login_form.is_valid():
            sith = login_form.cleaned_data.get('choice').first()
            auth.login(request, sith)
            return HttpResponseRedirect(reverse('sith:sith_list'))
    context = {
        'title': 'Вход для Ситхов',
        'login_form': login_form,
    }
    return render(request, 'sith_app/index.html', context)


@login_required
def sith_list(request):
    """View for rendering of Sith choice page"""
    master = Sith.get_item(request.user.pk)
    queryset = master.get_not_shadow_hand_sith_no_self()
    label = 'Выберите Ситха, которого зачислите Рукой Тени'
    choice_form = SithForm(queryset=queryset, label=label)
    if request.method == 'POST':
        choice_form = SithForm(queryset=queryset, label=label,
                               data=request.POST, files=request.FILES)
        if choice_form.is_valid():
            if master.get_shadow_hands_number >= SHADOW_HANDS_MAX_NUMBER:
                LOGGER.error('Ошибка при зачислении. Превышено максимальное число Рук Тени.')
            else:
                chosen_sith = choice_form.cleaned_data.get('choice').first()
                chosen_sith.turn_into_shadow_hand(master)
                if master.send_enrollment_mail(chosen_sith):
                    LOGGER.info('Сообщение о зачислении отправлено')
                else:
                    LOGGER.info('Ошибка отправки сообщения о зачислении')
            return HttpResponseRedirect(reverse('sith:shadow_hands_list'))
    context = {
        'title': 'Выбрать Руку Тени',
        'not_shadow_hand': queryset,
        'choice_form': choice_form,
    }
    return render(request, 'sith_app/sith_list.html', context)


def shadow_hands_list(request):
    """View for rendering of page with sith list"""
    sith_set = Sith.get_items()
    sith_with_two_and_more = [sith for sith in sith_set if sith.get_shadow_hands_number > 1]
    context = {
        'title': 'Список Ситхов',
        'sith_set': sith_set,
        'sith_with_two_and_more': sith_with_two_and_more,
    }
    return render(request, 'sith_app/shadow_hands_list.html', context)
