# Generated by Django 2.1.7 on 2019-02-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author_mail',
            field=models.EmailField(default='mail@test.ru', max_length=254),
            preserve_default=False,
        ),
    ]
