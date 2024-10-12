"""main_app URL Configuration"""
from django.urls import path
import main_app.views as main_app

app_name = 'main_app'
urlpatterns = [
    path('', main_app.main_page, name='main'),
    path('logout/', main_app.logout, name='logout'),
    path('login/', main_app.login, name='login'),
    path('to_sith/', main_app.to_sith, name='to_sith'),
]
