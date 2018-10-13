from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.question_form_view, name='question-form'),
]