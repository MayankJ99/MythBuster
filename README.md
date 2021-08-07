## Programming Myth Buster Hub

### Front End

After pulling the repository, go into the frontend folder

```
cd ./frontend
```

Install dependencies

```
npm i
```

OR

```
npm install
```

Create an ENV file with reference to the Back End API

Example: .env.development

```
VUE_APP_API_URL=http://localhost:8000
```

You may start the front end by running

```
npm run serve
```

### Backend API
Branch name: DRF

Built using Django DRF

MVP currently includes models for the following :-

* User
* User Profile
* Question
* Question Upvote
* Answer
* Answer Upvote

Models can be reviewed within users/models.py

### API guide and documentation

Myth buster folder

Contains config files for Django. Useless mostly.

Users folder

Users/urls/ —> contains the routes for the API. Each route has the route, function to call, and a name for the route

Users/views/ —> contains the API functions.

Each of these folders have been broken down into users and feed  to better modularize them.


models.py —> contains the DB schema for all the objects.
admin.py —> contains registration of the DB classes for the admin panel. This is how we can see and interact with the models within the admin panel.


### API ROUTES

For user api routes, we use the following prefix

http://localhost:8000/api/users

The routes within users is as follows

* /all/ —> returns all users in the database

* /{pk}/ —> uses the primary key or id of the user as a URL parameter. Returns user of that ID.   for eg: http://localhost:8000/api/users/2

* /login/ —> Login

* /register/ --> Register

* /profile/ --> returns currently logged in user

* /updateUser/ --> updates user and user profile details

* /deleteUser/  --> deletes user and user profile

Login will return 3 tokens, access, refresh and a token. Access token and Token token are interchangeable. To use access token for protected routes

Key should be Authorization
Value should be
“Bearer {token}”

For the feed routes, we use the following prefix

http://localhost:8000/api/feed

The routes are as follows

* /questions/all/ — return all the questions.
* /questions/{pk}/ —> return particular question of Primary Key / ID. Similar to how users work.
* /createQuestion — create a new question
* /updateQuestion/{pk}/ -- updates Question of Primary Key of ID
* /deleteQuestion/{pk}/ -- deletes Question of Primary Key of ID
* /upvoteQuestion/{pk}/ -- upvotes Question of Primary Key of ID
* /downvoteQuestion/{pk}/ -- removes upvote for Question of Primary Key of ID

* /questions/all/ — return all the answers. ( kinda useless )
* /questions/{pk}/ —> return all answers related to the question of Primary Key / ID. Similar to how users work.
* /createAnswer/{pk}/— create a new answer related to the question of Primary Key / ID. Similar to how users work.
* /updateAnswer/{pk}/ -- updates Answer of Primary Key of ID
* /deleteQuestion/{pk}/ -- deletes Answer of Primary Key of ID
* /upvoteQuestion/{pk}/ -- upvotes Answer of Primary Key of ID
* /downvoteQuestion/{pk}/ -- removes upvote for Answer of Primary Key of ID

* tag/{str:tag}/ --> returns questions of all the related tag slug


### Installation and Setup
* cd into /backend
* run pip install -r requirements.txt
* cd into backend/mythbuster
* run python manage.py makemigrations
* run python manage.py migrate
* run python manage.py runserver


=======
- Web Development
- Back end development
- Cloud Hosting
- Database Design

### Links

- [**Figma Deisgn**](https://www.figma.com/file/WLTnyGZKwMNvhOSAfOfqhC/Web-UI?node-id=0%3A1)
- [**Backend API**](https://github.com/MayankJ99/MythBuster/tree/DRF)

