# Generated by Django 2.1.7 on 2019-03-31 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='whats_news',
            field=models.BooleanField(default=False),
        ),
    ]
