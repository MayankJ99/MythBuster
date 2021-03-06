from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model

CurrentUser = get_user_model()


class User(CurrentUser, auth_models.PermissionsMixin):

    def __str__(self):
        return "{}".format(self.username)

class UserProfile(models.Model):
    user = models.OneToOneField(CurrentUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='media', blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedin = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)


    def __str__(self):  
        return "{}'s profile".format(self.user)


class Tags(models.Model):
    tag_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ('tag_name',)
        unique_together = ('tag_name',)

class Question(models.Model):
    user = models.ForeignKey(CurrentUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modifed_at = models.DateTimeField(auto_now=True)
    question_upvotes = models.ManyToManyField(CurrentUser, related_name='question_upvotes', blank=True)
    tags = models.ManyToManyField(Tags, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.question_text)


#create a model called answer with a foreign key relationship to question with the fields for title, content, created_at, user, modifed_at
class Answer(models.Model):
    user = models.ForeignKey(CurrentUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modifed_at = models.DateTimeField(auto_now=True)
    #create a field called answer_upvotes that is a many to many relationship with CurrentUser
    answer_upvotes = models.ManyToManyField(CurrentUser, related_name='answer_upvotes', blank=True)
    def __str__(self):
        return "{}".format(self.answer_text)
