# Generated by Django 4.1.1 on 2023-05-28 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='lang',
        ),
    ]
