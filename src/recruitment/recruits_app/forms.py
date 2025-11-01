"""Forms for recruit_app."""
from random import choice

from django import forms
from django.contrib.auth.forms import UserCreationForm

from recruitment.common import set_attributes
from recruitment.main_app.models import Question, QuestionSet
from recruitment.recruits_app.models import Recruit


class RecruitRegisterForm(UserCreationForm):
    """Class for recruit register form."""

    class Meta:
        """
        Class determines, which fields of model will be represented in form.

        """

        model = Recruit
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'planet',
            'age',
        )

    def __init__(self, *args, **kwargs):
        """Adding of attributes to fields."""
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            set_attributes(field)

    def age_validator(self):
        """Check recruit age."""
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('You are too young for recruit!')
        return data

    def save(self, commit=True):
        """Save new recruit."""
        user = super().save(commit=commit)
        user.question_set = choice(QuestionSet.get_items())
        user.save()
        return user


class QuestionForm(forms.ModelForm):
    """Class for question form."""

    class Meta:
        """
        Class determines, which fields of model will be represented in form.

        """

        model = Question
        exclude = ['code']

    def __init__(self, *args, **kwargs):
        """Adding of attributes to fields."""
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            set_attributes(field)
            if field_name == 'question':
                cls_attr = field.widget.attrs['class']
                field.widget.attrs['class'] = '{0}-plaintext'.format(cls_attr)
                field.widget.attrs['rows'] = '2'
                field.widget.attrs['readonly'] = 'readonly'
