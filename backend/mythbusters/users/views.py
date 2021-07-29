from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.


#create a rest api GET call view which will use the serializer for the question model and return all the questions in the DataBase
@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


#create a rest api GET call view which uses the serializer for the question model and returns a specific question in the DataBase
@api_view(['GET'])
def get_question(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)

#create a rest api POST call view which uses the serializer for the question model and creates a new question in the DataBase
# @api_view(['POST'])
# def create_question(request):
#     serializer = QuestionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)

#     return Response(serializer.errors)

#create a GET call for the answer model that gets all the answers from the database
@api_view(['GET'])
def get_answers(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

#create a GET call for the answer model that gets a specific answer from the database
@api_view(['GET'])
def get_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(answer)
    return Response(serializer.data)

