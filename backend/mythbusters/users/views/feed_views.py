from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from users.serializers import *
from users.models import *
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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

# create a rest api POST call view which uses the serializer for the question model and creates a new question in the DataBase
@api_view(['POST'])
def create_question(request):
    user = CurrentUser.objects.all()[0]
    print(user)

    question = Question.objects.create(
        user=user,
        title=request.data['title'],
        question_text = request.data['question_text']
    )

    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_answers(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

#create a get call that takes a PK for the question model and returns all answer objects that are related to that question
@api_view(['GET'])
def get_answers_for_question(request, pk):
    answers = Answer.objects.filter(question=pk)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


#create a POST call that takes a PK for the question model and a new answer object and saves it to the database
@api_view(['POST'])
def create_answer(request, pk):
    user = CurrentUser.objects.all()[1]
    print(user)
    question = Question.objects.get(id=pk)

    answer = Answer.objects.create(
        user=user,
        question=question,
        title=request.data['title'],
        answer_text = request.data['answer_text']
    )

    serializer = AnswerSerializer(answer, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



