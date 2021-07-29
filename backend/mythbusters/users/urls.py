from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.urls import path
from . import views

urlpatterns = [

    path('getQuestions/', views.get_questions, name='questions'),
    path('getQuestion/<str:pk>', views.get_question, name='question'),

    path('getAnswers/', views.get_answers, name='answers'),
    path('getAnswer/<str:pk>', views.get_answer, name='answer'),
]