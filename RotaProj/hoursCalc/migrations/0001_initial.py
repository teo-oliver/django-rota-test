# Generated by Django 2.1.2 on 2018-12-08 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HoursDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in', models.DateTimeField(blank=True, null=True)),
                ('clock_out', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('duration', models.FloatField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(blank=True, max_length=150, null=True)),
                ('month_hours', models.FloatField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(blank=True, max_length=150, null=True)),
                ('week_hours', models.FloatField(default=0)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoursCalc.Month')),
            ],
        ),
    ]
