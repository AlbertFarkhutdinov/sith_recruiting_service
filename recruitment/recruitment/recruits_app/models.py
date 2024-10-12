"""Models for recruits_app"""
from django.db import models
from recruitment.main_app.models import CustomUser, Planet, QuestionSet
from recruitment.sith_app.models import Sith
from recruitment.common import get_items, get_item


class Recruit(CustomUser):
    """Class for recruit model"""

    class Meta:
        """Correct representation of model in the admin interface"""
        verbose_name = 'Recruit'
        verbose_name_plural = 'Recruits'

    planet = models.ForeignKey(
        Planet,
        verbose_name='Planet',
        on_delete=models.CASCADE,
    )
    question_set = models.ForeignKey(
        QuestionSet,
        verbose_name='Test Task',
        on_delete=models.CASCADE,
        default=1,
    )

    @staticmethod
    def get_items(value=None, parameter=None):
        """Method returns all recruits,
        if value and parameter is None,
        else returns filtered queryset"""
        return get_items(Recruit, value=value, parameter=parameter)

    @staticmethod
    def get_item(value, parameter='pk'):
        """Method returns recruit with specified parameter"""
        return get_item(Recruit, value, parameter)

    def change_role(self, answers):
        """Method turns recruit to new sith"""
        user = CustomUser.get_item(self.pk)
        attributes = {}
        for key, value in user.__dict__.items():
            if key[0] != '_' and key != 'id':
                attributes[key] = value
        attributes['role'] = 'S'
        attributes['question_set'] = self.question_set
        attributes['answers'] = ''.join(answers)
        user.delete()
        Sith(planet=self.planet, **attributes).save()
        self.delete()
