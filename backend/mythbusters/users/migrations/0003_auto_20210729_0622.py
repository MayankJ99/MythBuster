# Generated by Django 3.2.4 on 2021-07-29 06:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20210729_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_upvotes',
            field=models.ManyToManyField(blank=True, related_name='answer_upvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='AnswerUpvote',
        ),
    ]
