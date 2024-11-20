from django.db import models
from django.core.exceptions import ValidationError


class FeedBack(models.Model):

    def validate_image_size(image):
        """
        Validate that the uploaded image does not exceed 5 MB.
        """
        max_size_in_mb = 2
        if image.size > max_size_in_mb * 1024 * 1024:
            raise ValidationError(f"The maximum file size that can be uploaded is {max_size_in_mb} MB.")


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
    image = models.ImageField(upload_to='feedback_images/', validators=[validate_image_size])

    def __str__(self):
        return f"{self.name} ({self.course})"
# Create your models here.
