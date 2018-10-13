from django.shortcuts import render
from django.http import HttpResponse

# from django.views.generic.edit import FormView # https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-editing/

from django.views.generic import TemplateView # https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-display/#generic-views-of-objects
from . import forms

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

index_view = IndexView.as_view()

class QuestionFormView(TemplateView):
    template_name = 'question-form.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionFormView, self).get_context_data(**kwargs)
        
        # data = {
        #     'form-TOTAL_FORMS': '',
        #     'form-INITIAL_FORMS': '',
        #     'form-MAX_NUM_FORMS': '',
        # }
        context['question_formset'] = forms.QuestionFormSet(
            # instance=forms.QuestionForm
            # data,
            # initial=[
            #     {
            #         'description': 'This is a default question description',
            #         'title': 'Question 1'
            #     }
            # ]
        )
        return context

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))
    
    def post(self, request, **kwargs):
        print('\n===== Posted! =====')
        print(kwargs)
        print('\n')
        return render(request, self.template_name, self.get_context_data(**kwargs))        

question_form_view = QuestionFormView.as_view()