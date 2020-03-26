"""Models for sith_app"""
from django.db import models
from django.core.mail import send_mail
from main_app.models import CustomUser, Planet, QuestionSet
from common import get_items, get_item, QUESTIONS_NUMBER_IN_SET


class Sith(CustomUser):
    """Class for sith model"""
    class Meta:
        """Correct representation of model in the admin interface"""
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    planet = models.ForeignKey(Planet,
                               verbose_name='Планета, на которой обучает',
                               on_delete=models.CASCADE)
    is_shadow_hand = models.BooleanField(verbose_name='Рука Тени',
                                         default=False)
    question_set = models.ForeignKey(QuestionSet,
                                     verbose_name='Тестовое испытание',
                                     on_delete=models.CASCADE,
                                     default=1)
    answers = models.CharField(verbose_name='Ответы',
                               max_length=QUESTIONS_NUMBER_IN_SET,
                               default='')
    master = models.ForeignKey('self',
                               verbose_name='Мастер',
                               on_delete=models.CASCADE,
                               related_name='shadow_hands',
                               null=True)

    @staticmethod
    def get_items(value=None, parameter=None):
        """Method returns all sith,
        if value and parameter is None,
        else returns filtered queryset"""
        return get_items(Sith, value=value, parameter=parameter)

    @staticmethod
    def get_item(value, parameter='pk'):
        """Method returns sith with specified parameter"""
        return get_item(Sith, value, parameter)

    def get_not_shadow_hand_sith_no_self(self):
        """Method returns all sith who is not Shadow Hand and not instance"""
        return Sith.get_items(parameter='is_shadow_hand', value=False).exclude(pk=self.pk)

    def get_shadow_hands(self):
        """Method returns list of Shadow Hands of Sith"""
        shadow_hands_list = self.shadow_hands.select_related()
        return shadow_hands_list

    def send_enrollment_mail(self, user):
        """Method sends enrollment mail to user"""
        title = f'Уведомление о зачислении Рукой Тени для Ситха {user.username}'
        message = '\n'.join([f'Приветствую, {user.username}! '
                             f'Ты зачислен Рукой Тени к Ситху {self.username}.'])
        return send_mail(
            title,
            message,
            self.email,
            [user.email],
            fail_silently=False
        )

    def turn_into_shadow_hand(self, master):
        """Method turns sith to Shadow Hand of specified master"""
        self.is_shadow_hand = True
        self.master = master
        self.save()

    @property
    def get_shadow_hands_number(self):
        """Method returns number of Shadow Hands of Sith"""
        return len(self.get_shadow_hands())
