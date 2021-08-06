from django.contrib import admin

# Register your models here.
from .models import *

#register all models from mythbusters
admin.site.register(UserProfile)
#regiser model for question, answer, questionUpvotes and answerUpvote
admin.site.register(Question)
admin.site.register(Answer)
# admin.site.register(QuestionUpvote)
# admin.site.register(AnswerUpvote)

admin.site.register(Tags)
