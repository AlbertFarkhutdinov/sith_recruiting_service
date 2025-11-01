"""recruits_app URL Configuration."""
from django.urls import path

from recruitment.recruits_app import views as recruits_app_views

app_name = 'recruits_app'
urlpatterns = [
    path('', recruits_app_views.register, name='register'),
    path('result/', recruits_app_views.result, name='result'),
    path(
        'shadow_hand_test/',
        recruits_app_views.QuestionList.as_view(),
        name='question_list',
    ),
]
