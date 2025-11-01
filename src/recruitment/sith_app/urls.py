"""sith_app URL Configuration."""
from django.urls import path

from recruitment.sith_app import views as sith_app_views

app_name = 'sith_app'
urlpatterns = [
    path('', sith_app_views.sith_login, name='sith_login'),
    path('sith_list/', sith_app_views.sith_list, name='sith_list'),
    path(
        'shadow_hands_list/',
        sith_app_views.shadow_hands_list,
        name='shadow_hands_list',
    ),
]
