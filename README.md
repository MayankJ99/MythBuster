## Programming Myth Buster Hub

###Backend API
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

URL Routes for API

- /createQuestion --> POST --> sends form data for the creation of a question instance
- /createAnswer/{pk} --> POST --> sends form data for the creation of an answer instance using URL param as Primary key for the question instance 
- /getQuestions/all --> GET --> returns a JSON list of all the question instances
- /getQuestions/{pk} --> GET --> returns a JSON res of the specific question instance as per PK
- /getAnswers/all --> GET --> returns a JSON list of all answer instances (for API testing purposes only)
- /getAnswers/{pk} --> GET --> returns JSON list of all answer objects that are related to the question with ID of PK

TODO for Backend:

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

#### WIP

### Objectives

- A platform where Programmers can post topics or opinions to be discussed and scrutinized. For example:
    - "GNU C++ compilation is less memory intensive than GNU Rust w/ LLVM".
    - "Javascript does not differentiate between float and integer types at runtime"


### Features

- User accounts
    - Tracks previous posts made by a user
    - User "track record" for quality of posts and responses
- Public topics may be created using text, videos, images, and other multimedia
    - Public topics may include the "goal post" of proving or debunking the myth
- Responses to public topics may be created using text, videos, images, and other multimedia
- Responses may be voted on as to whether or not the community accepts the response as an answer that meets the requirements of proving or debunking the myth
- Topics may be categorized


### Target Audience

- Intermediate programmers, self-taught and in University
    - When a programmer is in their learning stage, jumping from language to language and framework to framework, they have to swim through an ocean of facts, opinions, and lies which may be difficult to discern.
    - An archive of facts may be build related to these programming myths that may be referenced when discussing or deciding between languages and frameworks


- Experienced Developers
    - Experienced developers may be provided with a platform to discuss and document these topics that have been up for debate in the programming community.


### Resources & Skills

- Web Development
- Back end development
- Cloud Hosting
- Database Design
- Mobile App Development (Possibly)
