# Generated by Django 5.1.3 on 2024-11-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_alter_feedback_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
