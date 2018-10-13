from django import forms

from django.forms import formset_factory

class QuestionForm(forms.Form):
    title = forms.CharField() # Fields in Form https://docs.djangoproject.com/en/1.11/ref/forms/fields/#built-in-field-classes
    description = forms.CharField()

class AnswerForm(forms.Form):
    description = forms.CharField()
    correct = forms.BooleanField()

class BaseQuestionFormset(forms.BaseFormSet):
    
    def add_fields(self, form, index):
        super(BaseQuestionFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = AnswerFormSet(
            # instance=form.instance,
            # data=form.data if form.is_bound else None,
            # files=form.files if form.is_bound else None,
            prefix='answer-%s-%s' % (
                form.prefix,
                AnswerFormSet.get_default_prefix()),
            # extra=1
        )

QuestionFormSet = formset_factory(QuestionForm, formset=BaseQuestionFormset,
    extra=2,
    max_num=10,
    can_order=True,
    can_delete=True
) # Formset https://docs.djangoproject.com/en/1.11/topics/forms/formsets/

AnswerFormSet = formset_factory(AnswerForm,
    extra=1,
    max_num=10,
    can_order=True,
    can_delete=True
)