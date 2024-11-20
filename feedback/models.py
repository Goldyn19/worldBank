from django.db import models


class FeedBack(models.Model):

    SEX_OPTION = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    EMPLOYMENT_STATUS_OPTION = (
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('self-employed', 'Self-Employed'),
        ('student', 'student')
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    trainee_number = models.CharField(max_length=100, unique=True)
    course = models.CharField(max_length=255)
    nin = models.CharField(max_length=20, unique=True)
    sex = models.CharField(max_length=10, choices=SEX_OPTION)
    employment_status = models.CharField(max_length=25, choices=EMPLOYMENT_STATUS_OPTION)
    overall_rating = models.CharField(max_length=10)
    instructor_rating = models.CharField(max_length=10)
    skills_gained = models.TextField()
    skills_application = models.TextField()
    suggestions = models.TextField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.course})"
# Create your models here.
