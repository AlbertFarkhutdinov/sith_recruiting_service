"""Models for main_app"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from common import get_items, get_item


class CustomUser(AbstractUser):
    """Class for user model"""
    age = models.PositiveIntegerField(verbose_name='Возраст',
                                      default=18)
    email = models.EmailField(verbose_name='E-mail',
                              max_length=64,
                              unique=True)
    role = models.CharField(verbose_name='Роль',
                            max_length=1,
                            choices=(
                                ('S', 'Ситх'),
                                ('R', 'Рекрут'),
                            ),
                            default='R')

    @staticmethod
    def get_items(value=None, parameter=None):
        """Method returns all users,
        if value and parameter is None,
        else returns filtered queryset"""
        return get_items(CustomUser, value=value, parameter=parameter)

    @staticmethod
    def get_item(value, parameter='pk'):
        """Method returns user with specified parameter"""
        return get_item(CustomUser, value, parameter)

    def __str__(self):
        """String representation of model"""
        return self.username


class Planet(models.Model):
    """Class for planet model"""
    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface"""
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    name = models.CharField(verbose_name='Наименование',
                            max_length=32,
                            unique=True)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)

    @staticmethod
    def get_items(value=None, parameter=None):
        """Method returns all planets,
        if value and parameter is None,
        else returns filtered queryset"""
        return get_items(Planet, value=value, parameter=parameter)

    @staticmethod
    def get_item(value, parameter='pk'):
        """Method returns planet with specified parameter"""
        return get_item(Planet, value, parameter)

    def __str__(self):
        """String representation of model"""
        return self.name


class QuestionSet(models.Model):
    """Class for question set model"""
    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface"""
        verbose_name = 'Тестовое испытание'
        verbose_name_plural = 'Тестовые испытания'

    code = models.PositiveIntegerField(verbose_name='Уникальный код ордена',
                                       unique=True)
    created = models.DateTimeField(verbose_name='Время создания',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Время обновления',
                                   auto_now=True)

    def question_attributes(self, attribute='code'):
        """Method returns list of question attributes in set as the string"""
        question_list = self.questions.select_related()
        result = []
        if attribute == 'code':
            result = [str(question.code) for question in question_list]
        elif attribute == 'right_answer':
            result = [str(question.right_answer) for question in question_list]
        return ','.join(result)

    @property
    def question_numbers(self):
        """Method returns list of question codes in set as the string"""
        return self.question_attributes('code')

    @property
    def question_answers(self):
        """Method returns list of question answers in set as the string"""
        return self.question_attributes('right_answer')

    @staticmethod
    def get_items(value=None, parameter=None):
        """Method returns all question sets,
        if value and parameter is None,
        else returns filtered queryset"""
        return get_items(QuestionSet, value=value, parameter=parameter)

    @staticmethod
    def get_item(value, parameter='pk'):
        """Method returns question_set with specified parameter"""
        return get_item(QuestionSet, value, parameter)

    def __str__(self):
        """String representation of model"""
        return f'Тестовое испытание #{self.code}'


class Question(models.Model):
    """Class for question model"""
    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface"""
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    code = models.PositiveIntegerField(verbose_name='Код вопроса',
                                       unique=True)
    question_set = models.ForeignKey(QuestionSet,
                                     related_name="questions",
                                     verbose_name='Тестовое испытание',
                                     on_delete=models.CASCADE)
    question = models.TextField(verbose_name='Вопрос')
    right_answer = models.TextField(verbose_name='Ответ',
                                    choices=(
                                        ('Y', 'Да'),
                                        ('N', 'Нет')
                                    ),
                                    max_length=1)

    @staticmethod
    def get_items(value, parameter='question_set'):
        """Method returns questions for current question_set"""
        return get_items(Question,
                         value=value,
                         parameter=parameter)

    def __str__(self):
        """String representation of model"""
        return self.question
