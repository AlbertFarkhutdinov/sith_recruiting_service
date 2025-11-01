"""Representation of models from recruits_app in the admin interface."""
from django.contrib import admin

from recruitment.main_app.models import Question, QuestionSet
from recruitment.recruits_app.models import Recruit


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    """Representation of Recruit model in the admin interface."""

    list_display = (
        'username',
        'first_name',
        'last_name',
        'age',
        'email',
        'planet',
    )
    search_fields = ('username',)


@admin.register(QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    """Representation of QuestionSet model in the admin interface."""

    list_display = ('code', 'question_numbers')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Representation of Question model in the admin interface."""

    list_display = ('code', 'question', 'right_answer', 'question_set')
    list_filter = ('question_set',)
