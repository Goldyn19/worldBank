# Generated by Django 5.1.3 on 2024-11-20 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0012_alter_feedback_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='image',
        ),
    ]
