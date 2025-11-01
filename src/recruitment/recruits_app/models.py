"""Models for recruits_app."""
from django.db import models

from recruitment.common import get_item, get_items
from recruitment.main_app.models import CustomUser, Planet, QuestionSet
from recruitment.sith_app.models import Sith


class Recruit(CustomUser):
    """Class for recruit model."""

    class Meta:
        """Correct representation of model in the admin interface."""

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

    @classmethod
    def get_items(cls, value=None, parameter=None):
        """Return filtered queryset of Recruit instances."""
        return get_items(Recruit, value=value, parameter=parameter)

    @classmethod
    def get_item(cls, value, parameter='pk'):
        """Return recruit with specified parameter."""
        return get_item(Recruit, value, parameter)

    def change_role(self, answers):
        """Turn recruit to new sith."""
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
