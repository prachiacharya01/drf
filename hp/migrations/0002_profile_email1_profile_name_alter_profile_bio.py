# Generated by Django 4.0.3 on 2022-05-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email1',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
