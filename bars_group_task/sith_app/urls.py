"""sith_app URL Configuration"""
from django.urls import path
import sith_app.views as sith_app

app_name = 'sith_app'
urlpatterns = [
    path('', sith_app.sith_login, name='sith_login'),
    path('sith_list/', sith_app.sith_list, name='sith_list'),
    path('shadow_hands_list/', sith_app.shadow_hands_list, name='shadow_hands_list'),
]
