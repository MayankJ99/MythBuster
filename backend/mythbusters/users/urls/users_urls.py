from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.urls import path
from users.views.users_views import *


urlpatterns = [
    #add a url path for getting the users from the functions in views
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', create_user, name='register'),
    path('all/', get_users , name='getUsers'),
    path('updateUser/', update_user , name='updateUser'),
    path('deleteUser/', delete_user , name='deleteUser'),
    path('profile/' , get_current_user_profile , name='getUserProfile'),
    path('<str:pk>/', get_user_profile , name='getUserById'),
]