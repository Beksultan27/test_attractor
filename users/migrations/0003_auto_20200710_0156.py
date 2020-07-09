# Generated by Django 3.0.6 on 2020-07-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='nogi', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='kak u gogi', max_length=25),
        ),
    ]
