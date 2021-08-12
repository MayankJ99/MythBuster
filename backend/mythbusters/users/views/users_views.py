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

#create a GET view called get_current_user_profile that will be a protected route to return the current user's profile
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_current_user_profile(request):
    print(request.user)
    user = CurrentUser.objects.get(pk=request.user.id)
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


#create a PUT call to update a user in the User model in Django. It should include a permission for isauth users to update their own profile
#the PUT call should update the UserProfile model as well. It should only update the fields that are non empty in the request data
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_user(request):
    try:
        user = CurrentUser.objects.get(pk=request.user.id)
        user_profile = UserProfile.objects.get(user=user)

        data = request.data 

        # if data['username'] != '':
        #     user.username = data['username']
        # if data['email'] != '':
        #     user.email = data['email']
        # if data['first_name'] != '':
        #     user.first_name = data['first_name']
        # if data['last_name'] != '':
        #     user.last_name = data['last_name']
        # if data['bio'] != '':
        #     user_profile.bio = data['bio']
        # if data['linkedin'] != '':
        #     user_profile.linkedin = data['linkedin']
        # if data['twitter'] != '':
        #     user_profile.twitter = data['twitter']
        # if data['github'] != '':
        #     user_profile.github = data['github']
        # if data['occupation'] != '':
        #     user_profile.occupation = data['occupation']
        # if data['location'] != '':
        #     user_profile.location = data['location']
        # if data['website'] != '':
        #     user_profile.website = data['website']
        # if data['education'] != '':
        #     user_profile.education = data['education']
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'bio' in data:
            user_profile.bio = data['bio']
        if 'linkedin' in data:
            user_profile.linkedin = data['linkedin']
        if 'profile_image' in data:
            user_profile.profile_image = data['profile_image']
        if 'twitter' in data:
            user_profile.twitter = data['twitter']
        if 'github' in data:
            user_profile.github = data['github']
        if 'occupation' in data:
            user_profile.occupation = data['occupation']
        if 'location' in data:
            user_profile.location = data['location']
        if 'website' in data:
            user_profile.website = data['website']
        if 'education' in data:
            user_profile.education = data['education']
        
        user.save()
        user_profile.save()

        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        message = {"error" : err}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#create a DELETE call to delete the current user from the User model in Django. Must be protected by a permission class
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_user(request):
    try:
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        message = {"error" : err}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    






