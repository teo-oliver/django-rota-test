# Generated by Django 2.1.2 on 2019-01-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoursCalc', '0007_shift_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ['-date']},
        ),
    ]
