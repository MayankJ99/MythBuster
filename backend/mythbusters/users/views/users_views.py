from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from users.serializers import *
from users.models import *
# Create your views here.
from rest_framework import status
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#create a GET view to return all users from the User model in Django
@api_view(['GET'])
def get_users(request):
    
    users = CurrentUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#create a GET view to return one particular user from the User model in Django using the pk
@api_view(['GET'])
def get_user_profile(request, pk):
    user = CurrentUser.objects.get(pk=pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

#create a POST view to create a new user in the User model in Django that also creates a UserProfile object associated with the newly created user
@api_view(['POST'])
def create_user(request):
    try:
        data = request.data
        print(data)

        user = CurrentUser.objects.create(
            username=data['username'],
            email = data['email'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            password=make_password(data['password']),
        )
    

        user_profile = UserProfile.objects.create(
            user=user,
            bio=data['bio'],
            linkedin=data['linkedin'],
            twitter = data['twitter'],
            github = data['github'],
            occupation = data['occupation'],
            location = data['location'],
            website = data['website'],
            education = data['education'],
        )
        user.save()
        user_profile.save()

        serializer = UserSerializerWithToken(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)










