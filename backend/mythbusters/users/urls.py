from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.urls import path
from . import views

urlpatterns = [

    path('getQuestions/all', views.get_questions, name='questions'),
    path('getQuestions/<str:pk>', views.get_question, name='question'),
    path('createQuestion', views.create_question, name='createQuestion'),

    path('getAnswers/all', views.get_answers, name='answers'),
    path('getAnswers/<str:pk>', views.get_answers_for_question, name='answer'), 
    path('createAnswer/<str:pk>', views.create_answer, name='createQuestion'),
]