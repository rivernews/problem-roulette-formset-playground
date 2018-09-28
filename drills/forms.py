from django import forms

from django.forms import formset_factory

class QuestionForm(forms.Form):
    title = forms.CharField() # Fields in Form https://docs.djangoproject.com/en/1.11/ref/forms/fields/#built-in-field-classes
    description = forms.CharField()

class AnswerForm(forms.Form):
    description = forms.CharField()
    correct = forms.BooleanField()

AnswerFormSet = formset_factory(AnswerForm,
    extra=2,
    max_num=10
) # Formset https://docs.djangoproject.com/en/1.11/topics/forms/formsets/