# Generated by Django 4.1.1 on 2024-04-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_alter_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
