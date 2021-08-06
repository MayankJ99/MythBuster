## Programming Myth Buster Hub

### Backend API
Branch name: DRF


Built using Django DRF

MVP currently includes models for the following :-

- User
- User Profile
- Question
- Question Upvote
- Answer 
- Answer Upvote

Models can be reviewed within users/models.py

## URL Routes for API

- /createQuestion --> POST --> sends form data for the creation of a question instance
- /createAnswer/{pk} --> POST --> sends form data for the creation of an answer instance using URL param as Primary key for the question instance 
- /getQuestions/all --> GET --> returns a JSON list of all the question instances
- /getQuestions/{pk} --> GET --> returns a JSON res of the specific question instance as per PK
- /getAnswers/all --> GET --> returns a JSON list of all answer instances (for API testing purposes only)
- /getAnswers/{pk} --> GET --> returns JSON list of all answer objects that are related to the question with ID of PK

## TODO for Backend:

- Add models for tagging or use Django Taggit
- Add models for comments under answers or questions.
- Add Auth flow for registering/logging in users
- Add protected routes for creating questions/answers
- Add Update/Delete routes for questions and answers
- Add CRUD routes for upvoting for both questions and answers
- Add CRUD routes for user profile 
- Add support for media queries, preferably using AWS S3 for storage
- Add testing for API routes
- Host Website

## Installation

- cd into /backend
- run pip install -r requirements.txt
- cd into backend/mythbuster
- run python manage.py makemigrations
- run python manage.py migrate
- run python manage.py runserver


Go to localhost:8000/ for API
=======
- Web Development
- Back end development
- Cloud Hosting
- Database Design

### Links

- [**Figma Deisgn**](https://www.figma.com/file/WLTnyGZKwMNvhOSAfOfqhC/Web-UI?node-id=0%3A1)
- [**Backend API**](https://github.com/MayankJ99/MythBuster/tree/DRF)

