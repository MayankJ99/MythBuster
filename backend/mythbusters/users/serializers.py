from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


#create a serializer for the Tags model that will return the name of the Tag rather than the pk
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_name']

#from the Question model create a serializer for all the fields
class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    count = serializers.SerializerMethodField('answer_count')
    tags = TagSerializer(many=True, read_only=True)
    

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

#create a serializer for the User model for django
class UserSerializer(serializers.ModelSerializer):
    # questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    # answers = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
    class Meta:
        model = User
        # fields = ('id', 'username', 'questions', 'answers')
        fields = ('id', 'username', 'email',)

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'token',]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

#create a serializer for the User model for Django including a primary key related field to UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')

    def get_profile(self, obj):
        profile = UserProfile.objects.get(user=obj)
        return ProfileSerializer(profile).data

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
   
