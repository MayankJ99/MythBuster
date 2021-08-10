from .models import *
from django.test import TestCase


#create a test case to retrieve all users from the API and assert it
class UserTestCase(TestCase):

    

    def test_get_users(self):
        response = self.client.get('/api/users/all/')
        print(response.data)
        self.assertEqual(response.status_code, 200)
    

#create a test class
class UserTest(TestCase):
    
    #create a test case to retrieve all users from the API and assert it

   
    def setUp(self):
        user_data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@test.com",
        "first_name": "test",
        "last_name": "user",
        "bio": "test bio",
        "location": "test location",
        "twitter" : "twitter",
        "linkedin" : "linkedin",
        "github" : "github",
        "website" : "website",
        "education" : "education",
        "occupation" : "occupation"
        }

        response = self.client.post('/api/users/register/', user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['id'], 1)

        response = self.client.post('/api/users/login/', {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['id'], 1)
        self.token = response.data['access']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_users(self):
        response = self.client.get('/api/users/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    #create a test case to retrieve a user and assert it
    def test_get_user(self):
        response = self.client.get('/api/users/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['id'], 1)

    #create a test to get current profile using authentication at /profile
    def test_get_current_profile(self):
        response = self.client.get('/api/users/profile/', HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['profile']['bio'] , 'test bio')

    
    #create a test case to delete a user and assert it
    def test_delete_user(self):
        response = self.client.delete('/api/users/deleteUser/', HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

        


    