from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

#from the Question model create a serializer for all the fields
class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    count = serializers.SerializerMethodField('answer_count')
    upvotes= serializers.SerializerMethodField('get_upvote_count') 

    def get_upvote_count(self, obj):
        return QuestionUpvote.objects.filter(question=obj).count()

    def answer_count(self, obj):
        return Answer.objects.filter(question=obj).count()
    
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {'username':{'required':False}}

#create a serializer for the anwser model
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
   
    class Meta:
        model = Answer
        fields = '__all__'