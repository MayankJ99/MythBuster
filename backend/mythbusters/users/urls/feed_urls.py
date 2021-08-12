
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.urls import path
from users.views.feed_views import *

urlpatterns = [

    path('questions/all/', get_questions, name='questions'),
    path('questions/<str:pk>/', get_question, name='question'),
    path('createQuestion/', create_question, name='createQuestion'),
    path('updateQuestion/<str:pk>/', update_question, name='updateQuestion'),
    path('deleteQuestion/<str:pk>/', delete_question, name='deleteQuestion'),
    path('upvoteQuestion/<str:pk>/', add_user_upvote_to_question, name='upvoteQuestion'),
    path('downvoteQuestion/<str:pk>/', remove_user_upvote_to_question, name='downvoteQuestion'),

    path('answers/all/', get_answers, name='answers'),
    path('answers/<str:pk>/', get_answers_for_question, name='answer'), 
    path('createAnswer/<str:pk>/', create_answer, name='createQuestion'),
    path('updateAnswer/<str:pk>/', update_answer, name='updateAnswer'),
    path('deleteAnswer/<str:pk>/', delete_answer, name='deleteAnswer'),
    path('upvoteAnswer/<str:pk>/', add_user_upvote_to_answer, name='upvoteAnswer'),
    path('downvoteAnswer/<str:pk>/', remove_user_upvote_to_answer, name='downvoteAnswer'),

    #get questions by tag name
    path('tag/<str:tag>', get_questions_by_tag, name='questions_by_tag'),
    #add a path to include a query string 
]

