from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.answer_form_view, name='answer-form'),
]