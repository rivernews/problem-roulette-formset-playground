from django.shortcuts import render
from django.http import HttpResponse

# from django.views.generic.edit import FormView # https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-editing/

from django.views.generic import TemplateView # https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-display/#generic-views-of-objects
from . import forms

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

index_view = IndexView.as_view()

class AnswerFormView(TemplateView):
    template_name = 'answer-form.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerFormView, self).get_context_data(**kwargs)
        context['formset'] = forms.AnswerFormSet(
            initial=[
                {
                    'description': 'This is a default answer',
                    'correct': True
                }
            ]
        )
        return context

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))

answer_form_view = AnswerFormView.as_view()