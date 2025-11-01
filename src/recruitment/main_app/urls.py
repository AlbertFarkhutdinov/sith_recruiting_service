"""main_app URL Configuration."""
from django.urls import path

from recruitment.main_app import views as main_app_views

app_name = 'main_app'
urlpatterns = [
    path('', main_app_views.main_page, name='main'),
    path('logout/', main_app_views.logout, name='logout'),
    path('login/', main_app_views.login, name='login'),
    path('to_sith/', main_app_views.to_sith, name='to_sith'),
]
