"""Models for main_app."""
from django.contrib.auth.models import AbstractUser
from django.db import models

from recruitment.common import get_item, get_items


class CustomUser(AbstractUser):
    """Class for user model."""

    age = models.PositiveIntegerField(
        verbose_name='Age',
        default=18,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=64,
        unique=True,
    )
    role = models.CharField(
        verbose_name='Role',
        max_length=1,
        choices=(
            ('S', 'Sith'),
            ('R', 'Recruit'),
        ),
        default='R',
    )

    @classmethod
    def get_items(cls, value=None, parameter=None):
        """Return filtered queryset of CustomUser instances."""
        return get_items(CustomUser, value=value, parameter=parameter)

    @classmethod
    def get_item(cls, value, parameter='pk'):
        """Return user with specified parameter."""
        return get_item(CustomUser, value, parameter)

    def __str__(self):
        """Return string representation of model."""
        return self.username


class Planet(models.Model):
    """Class for planet model."""

    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface."""

        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'

    name = models.CharField(
        verbose_name='Name',
        max_length=32,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
    )

    @classmethod
    def get_items(cls, value=None, parameter=None):
        """Return filtered queryset of Planet instances."""
        return get_items(Planet, value=value, parameter=parameter)

    @classmethod
    def get_item(cls, value, parameter='pk'):
        """Return planet with specified parameter."""
        return get_item(Planet, value, parameter)

    def __str__(self):
        """Return string representation of model."""
        return self.name


class QuestionSet(models.Model):
    """Class for question set model."""

    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface."""

        verbose_name = 'Test task'
        verbose_name_plural = 'Test tasks'

    code = models.PositiveIntegerField(
        verbose_name='Unique Code',
        unique=True,
    )
    created = models.DateTimeField(
        verbose_name='Creating Time',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Update Time',
        auto_now=True,
    )

    def question_attributes(self, attribute='code'):
        """Return list of question attributes in set as the string."""
        question_list = self.questions.select_related()
        result_list = []
        if attribute == 'code':
            result_list = [str(question.code) for question in question_list]
        elif attribute == 'right_answer':
            result_list = [
                str(question.right_answer) for question in question_list
            ]
        return ','.join(result_list)

    @property
    def question_numbers(self):
        """Return list of question codes in set as the string."""
        return self.question_attributes('code')

    @property
    def question_answers(self):
        """Return list of question answers in set as the string."""
        return self.question_attributes('right_answer')

    @classmethod
    def get_items(cls, value=None, parameter=None):
        """Return filtered queryset of QuestionSet instances."""
        return get_items(QuestionSet, value=value, parameter=parameter)

    @classmethod
    def get_item(cls, value, parameter='pk'):
        """Return question_set with specified parameter."""
        return get_item(QuestionSet, value, parameter)

    def __str__(self):
        """Return string representation of model."""
        return 'Test task #{0}'.format(self.code)


class Question(models.Model):
    """Class for question model."""

    objects = models.Manager()

    class Meta:
        """Correct representation of model in the admin interface."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    code = models.PositiveIntegerField(
        verbose_name='Question ID',
        unique=True,
    )
    question_set = models.ForeignKey(
        QuestionSet,
        related_name='questions',
        verbose_name='Test Task',
        on_delete=models.CASCADE,
    )
    question = models.TextField(verbose_name='Question')
    right_answer = models.TextField(
        verbose_name='Answer',
        choices=(
            ('Y', 'Yes'),
            ('N', 'No'),
        ),
        max_length=1,
    )

    @classmethod
    def get_items(cls, value, parameter='question_set'):
        """Return questions for current question_set."""
        return get_items(
            Question,
            value=value,
            parameter=parameter,
        )

    def __str__(self):
        """Return string representation of model."""
        return self.question
