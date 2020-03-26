"""recruits_app URL Configuration"""
from django.urls import path
import recruits_app.views as recruits_app

app_name = 'recruits_app'
urlpatterns = [
    path('', recruits_app.register, name='register'),
    path('shadow_hand_test/', recruits_app.QuestionList.as_view(), name='question_list'),
    path('result/', recruits_app.result, name='result'),
]
