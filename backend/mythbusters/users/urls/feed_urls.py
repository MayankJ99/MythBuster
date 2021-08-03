
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.urls import path
from users.views.feed_views import *

urlpatterns = [

    path('questions/all', get_questions, name='questions'),
    path('questions/<str:pk>', get_question, name='question'),
    path('createQuestion', create_question, name='createQuestion'),

    path('answers/all', get_answers, name='answers'),
    path('answers/<str:pk>', get_answers_for_question, name='answer'), 
    path('createAnswer/<str:pk>', create_answer, name='createQuestion'),
]