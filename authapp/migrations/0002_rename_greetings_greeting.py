# Generated by Django 4.1.7 on 2023-03-03 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Greetings',
            new_name='Greeting',
        ),
    ]
