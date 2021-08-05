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


# create a rest api POST call view which uses the serializer for the question model and creates a new question in the DataBase
#add permision for isauthenticated users to create a question
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_question(request):
    # user = CurrentUser.objects.all()[0]
    user = CurrentUser.objects.get(id=request.user.id)
    print(user)

    question = Question.objects.create(
        user=user,
        title=request.data['title'],
        question_text = request.data['question_text']
    )

    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)


#create a POST call that takes a PK for the question model and a new answer object and saves it to the database
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_answer(request, pk):
    # user = CurrentUser.objects.all()[1]
    user = CurrentUser.objects.get(id=request.user.id)
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


#create a PUT call that takes a PK for the question model and updates the question object with the new title and text
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_question(request, pk):
    question = Question.objects.get(id=pk)
    #check if request.data contains title 
    if 'title' in request.data:
        question.title = request.data['title']
    #check if request.data contains question_text
    if 'question_text' in request.data:
        question.question_text = request.data['question_text']
    question.save()
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)


#create a PUT call that takes a PK for the answer model and updates the answer object with the new title and text
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    #check if request.data contains title
    if 'title' in request.data:
        answer.title = request.data['title']
    #check if request.data contains answer_text
    if 'answer_text' in request.data:
        answer.answer_text = request.data['answer_text']
    answer.save()
    serializer = AnswerSerializer(answer, many=False)
    return Response(serializer.data)


#create a DELETE call that takes a PK for the question model and deletes the question object from the database
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_question(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    message = {message, 'Question deleted succesfully'}
    return Response(status=status.HTTP_204_NO_CONTENT)

#create a DELETE call that takes a PK for the answer model and deletes the answer object from the database
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()
    message = {'Answer deleted successfully'}
    return Response(message, status=status.HTTP_204_NO_CONTENT)


#to be added to urls.py

#create a protected PUT call takes the PK for the current question and creates a new upvote for that question where the current user is the user
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def add_user_upvote_to_question(request, pk):
    question = Question.objects.get(id=pk)
    user = CurrentUser.objects.get(id=request.user.id)
    question.question_upvotes.add(user)
    question.save()
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

#create a protected PUT call takes the PK for the current answer and creates a new upvote for that answer where the current user is the user
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def add_user_upvote_to_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    user = CurrentUser.objects.get(id=request.user.id)
    answer.answer_upvotes.add(user)
    answer.save()
    serializer = AnswerSerializer(answer, many=False)
    return Response(serializer.data)

#create a protected PUT call takes the PK for the current answer and removes a upvote for that answer where the current user is the user
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def remove_user_upvote_to_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    user = CurrentUser.objects.get(id=request.user.id)
    answer.answer_upvotes.remove(user)
    answer.save()
    serializer = AnswerSerializer(answer, many=False)
    return Response(serializer.data)

#create a protected PUT call takes the PK for the current question and removes a upvote for that question where the current user is the user
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def remove_user_upvote_to_question(request, pk):
    question = Question.objects.get(id=pk)
    user = CurrentUser.objects.get(id=request.user.id)
    question.question_upvotes.remove(user)
    question.save()
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)




