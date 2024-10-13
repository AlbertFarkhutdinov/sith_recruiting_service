"""Views for recruits_app."""
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import ListView

from recruitment.main_app.models import Question, QuestionSet
from recruitment.recruits_app.forms import QuestionForm, RecruitRegisterForm
from recruitment.recruits_app.models import Recruit


def register(request):
    """View for rendering of recruit register page."""
    register_form = RecruitRegisterForm()
    if request.method == 'POST':
        register_form = RecruitRegisterForm(
            data=request.POST,
            files=request.FILES,
        )
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('recruits:question_list'))
    context = {
        'title': 'Recruit Registration',
        'register_form': register_form,
    }
    return render(
        request=request,
        template_name='recruits_app/register.html',
        context=context,
    )


class IsRecruit(UserPassesTestMixin):
    """Mixin for checking if user is a recruit."""

    def test_func(self):
        """Method providing the test performance."""
        user = self.request.user
        return user.is_authenticated and user.role == 'R'


class QuestionList(IsRecruit, ListView):
    """CBV for rendering of Shadow Hand test page."""

    model = QuestionSet

    def get_context_data(self, **kwargs):
        """Edit context data."""
        context = super().get_context_data(**kwargs)
        question_set = Recruit.get_item(self.request.user.pk).question_set
        questions = Question.get_items(question_set)
        if questions:
            question_set = inlineformset_factory(
                parent_model=QuestionSet,
                model=Question,
                form=QuestionForm,
                extra=len(questions),
            )
            formset = question_set()
            for num, form in enumerate(formset.forms):
                form.initial['question'] = questions[num].question
                form.initial['right_answer'] = questions[num].right_answer
            context['question_set'] = formset
        return context


@login_required
def result(request):
    """View for rendering of result page."""
    context = {}
    if request.method == 'POST':
        data = request.POST
        answers = [data[key] for key in data.keys() if '-right_answer' in key]
        recruit = Recruit.get_item(request.user.pk)
        questions = Question.get_items(recruit.question_set)
        if answers == [question.right_answer for question in questions]:
            context['test_passed'] = True
            recruit.change_role(answers)
        else:
            context['test_passed'] = False
    return render(
        request=request,
        template_name='recruits_app/result.html',
        context=context,
    )
