# Generated by Django 5.1.3 on 2024-11-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_employment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='feedback_images/'),
        ),
    ]
