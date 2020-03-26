"""Forms for recruit_app"""
from django.contrib.auth.forms import UserCreationForm
from django import forms
from recruits_app.models import Recruit
from main_app.models import Question, QuestionSet
from random import choice
from common import set_attributes


class RecruitRegisterForm(UserCreationForm):
    """Class for recruit register form"""
    class Meta:
        """Class determines, which fields of model will be represented in form"""
        model = Recruit
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'planet', 'age')

    def __init__(self, *args, **kwargs):
        """Adding of attributes to fields"""
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            set_attributes(field)

    def age_validator(self):
        """Function for checking of recruit age"""
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды для рекрута!')
        return data

    def save(self, commit=True):
        """Function for saving of new recruit"""
        user = super(RecruitRegisterForm, self).save()
        user.question_set = choice(QuestionSet.get_items())
        user.save()
        return user


class QuestionForm(forms.ModelForm):
    """Class for question form"""
    class Meta:
        """Class determines, which fields of model will be represented in form"""
        model = Question
        exclude = ['code']

    def __init__(self, *args, **kwargs):
        """Adding of attributes to fields"""
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            set_attributes(field)
            if field_name == 'question':
                field.widget.attrs['class'] += '-plaintext'
                field.widget.attrs['rows'] = '2'
                field.widget.attrs['readonly'] = 'readonly'
