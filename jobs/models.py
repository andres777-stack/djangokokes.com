from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

class Job(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


AVAILABLE_DAYS =(
    ("1", "Lunes"),
    ("2", "Martes"),
    ("3", "Miercoles"),
    ("4", "Jueves"),
    ("5", "Viernes"),
)

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(message=f'{value} is in the past.', code='past_date')

class Applicant(models.Model):

    EMPLOYMENT_TYPE =(
    ("1", "Full-Time"),
    ("2", "Part-Time"),
    ("3", "Contract Work")
)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(help_text='A valid email address')
    website = models.URLField(blank=True, validators = [URLValidator(schemes=['http', 'https'])])
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=50)
    start_date = models.DateField( help_text= 'The earliest date you can start working', validators=[validate_future_date])
    available_days = models.CharField(max_length=50)
    desired_hourly_wage = models.DecimalField(max_digits=5, decimal_places=2)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to = 'private/resumes', blank=True, help_text='PDF only')
    confirmation = models.BooleanField()
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.job})'

# Create your models here.
