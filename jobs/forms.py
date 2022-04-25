from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(message=f'{value} is in the past.', code='past_date')

EMPLOYMENT_TYPE =(
    ("1", "Full-Time"),
    ("2", "Part-Time"),
    ("3", "Contract Work")
)

AVAILABLE_DAYS =(
    ("1", "Lunes"),
    ("2", "Martes"),
    ("3", "Miercoles"),
    ("4", "Jueves"),
    ("5", "Viernes"),
)

YEARS = range(2022, datetime.now().year+2)

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'pagina', 'size':'50'}), validators=[URLValidator(schemes=['http', 'https'])])
    #website = forms.URLField(widget=forms.URLInput(attrs={'size': '50', 
    #'placeholder': 'https://www.example.com'}))
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS, attrs={'style': 'width:31%; display: inline-block; margin: 0 1%'}), validators=[validate_future_date])
    available_days = forms.TypedMultipleChoiceField(choices=AVAILABLE_DAYS, coerce=int, widget=forms.CheckboxSelectMultiple(attrs={'checked': True}))
    desire_hourly_wage = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '10.10', 'max':'100.00', 'step':'.25'}))
    cover_letter = forms.CharField(max_length=50)
    command = forms.CharField(widget=forms.Textarea(attrs={'cols':'75', 'rows':'5'}))
    confirmation = forms.BooleanField(label="I certify that the information I have provided is true")
