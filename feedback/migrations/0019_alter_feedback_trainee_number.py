# Generated by Django 5.1.3 on 2025-02-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0018_alter_feedback_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='trainee_number',
            field=models.CharField(max_length=100),
        ),
    ]
