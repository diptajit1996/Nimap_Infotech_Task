# Generated by Django 4.2.5 on 2024-03-13 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_alter_usermodel_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
