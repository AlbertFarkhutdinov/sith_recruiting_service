"""Models for sith_app."""
from django.core.mail import send_mail
from django.db import models

from recruitment.common import QUESTIONS_NUMBER_IN_SET, get_item, get_items
from recruitment.main_app.models import CustomUser, Planet, QuestionSet


class Sith(CustomUser):
    """Class for sith model."""

    class Meta:
        """Correct representation of model in the admin interface."""

        verbose_name = 'Sith'
        verbose_name_plural = 'Siths'

    planet = models.ForeignKey(
        Planet,
        verbose_name='Planet',
        on_delete=models.CASCADE,
    )
    is_shadow_hand = models.BooleanField(
        verbose_name='Is Shadow Hand?',
        default=False,
    )
    question_set = models.ForeignKey(
        QuestionSet,
        verbose_name='Test Task',
        on_delete=models.CASCADE,
        default=1,
    )
    answers = models.CharField(
        verbose_name='Answers',
        max_length=QUESTIONS_NUMBER_IN_SET,
        default='',
    )
    master = models.ForeignKey(
        to='self',
        verbose_name='Master',
        on_delete=models.CASCADE,
        related_name='shadow_hands',
        null=True,
    )

    @classmethod
    def get_items(cls, value=None, parameter=None):
        """Return filtered queryset of Sith instances."""
        return get_items(Sith, value=value, parameter=parameter)

    @classmethod
    def get_item(cls, value, parameter='pk'):
        """Return sith with specified parameter."""
        return get_item(Sith, value, parameter)

    def get_not_shadow_hand_sith_no_self(self):
        """Return all sith who is not Shadow Hand and not instance."""
        return Sith.get_items(
            parameter='is_shadow_hand',
            value=False,
        ).exclude(pk=self.pk)

    def get_shadow_hands(self):
        """Return list of Shadow Hands of Sith."""
        return self.shadow_hands.select_related()

    def send_enrollment_mail(self, user):
        """Send enrollment mail to user."""
        username = user.username
        title = 'Shadow Hand Enrollment Notice for Sith {0}'.format(username)
        message = '\n'.join(
            [
                'Greetings, {0}! '.format(username),
                'You are the Shadow Hand of the Sith {0}.'.format(
                    self.username,
                ),
            ],
        )
        return send_mail(
            title,
            message,
            self.email,
            [user.email],
            fail_silently=False,
        )

    def turn_into_shadow_hand(self, master):
        """Turn sith to Shadow Hand of specified master."""
        self.is_shadow_hand = True
        self.master = master
        self.save()

    @property
    def get_shadow_hands_number(self):
        """Return number of Shadow Hands of Sith."""
        return len(self.get_shadow_hands())
