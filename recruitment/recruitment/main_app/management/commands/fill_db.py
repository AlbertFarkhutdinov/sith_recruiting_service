"""Module with settings for command 'python manage.py fill_db'"""
from json import load
from os.path import join
from django.core.management.base import BaseCommand
from django.conf import settings
from recruitment.main_app.models import Planet, Question, QuestionSet
from recruitment.sith_app.models import Sith
from recruitment.common import QUESTIONS_NUMBER_IN_SET


def load_from_json(file_name):
    """Function for loading data from json file"""
    with open(join(settings.JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as file:
        return load(file)


class Command(BaseCommand):
    """Class for command 'python manage.py fill_db'"""
    def handle(self, *args, **options):
        """Logic of command 'python manage.py fill_db'"""
        for model in (Planet, Sith, QuestionSet, Question):
            model.objects.all().delete()

        all_planets = load_from_json('planets')
        for planet in all_planets:
            Planet(**planet).save()

        all_questions = load_from_json('questions')
        set_code = 0
        for number, question in enumerate(all_questions):
            if number % QUESTIONS_NUMBER_IN_SET == 0:
                set_code += 1
                QuestionSet(code=set_code).save()
            question["question_set"] = QuestionSet.get_item(set_code, parameter='code')
            Question(**question).save()

        superuser_data = settings.SUPERUSER_DATA
        all_sith = load_from_json('sith')
        for i, sith in enumerate([superuser_data] + all_sith):
            sith["planet"] = Planet.get_item(sith["planet"], parameter='name')
            sith["role"] = 'S'
            if i == 0:
                Sith.objects.create_superuser(**sith)
            else:
                sith["master"] = Sith.get_item(sith["master"], parameter='username')
                Sith(**sith).save()
