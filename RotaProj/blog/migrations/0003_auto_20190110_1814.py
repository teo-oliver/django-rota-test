# Generated by Django 2.1.2 on 2019-01-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_todo_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=40),
        ),
    ]
