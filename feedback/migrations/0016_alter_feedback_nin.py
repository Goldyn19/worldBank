# Generated by Django 5.1.3 on 2025-02-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0015_alter_feedback_employment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='nin',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
