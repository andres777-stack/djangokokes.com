from django import forms

EMPLOYMENT_TYPE =(
    ("1", "Full-Time"),
    ("2", "Part-Time"),
    ("3", "Contract Work")
)

AVAILABLE_DAYS =(
    ("L", "Lunes"),
    ("M", "Martes"),
    ("MI", "Miercoles"),
    ("J", "Jueves"),
    ("V", "Viernes"),
)
class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)
    start_date = forms.DateField(help_text="The earliest date you can start working")
    available_days = forms.MultipleChoiceField(choices=AVAILABLE_DAYS, help_text="Select all days that you can work")
    desire_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField(max_length=50)
    confirmation = forms.BooleanField(label="I certify that the information I have provided is true")
