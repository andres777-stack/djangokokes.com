import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView

from common.utils.email import send_email
from jobs.models import Applicant
from .forms import JobApplicationForm 


class JobAppView(CreateView):
    model = Applicant
    template_name = 'jobs/applicant_form.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')
    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        to = 'ramirezsanmartinsergio@gmail.com'
        subject = 'Application for Joke Writer'
        content = f'<p>Hey HR manager!</p><p>Job application received:</p><ol>'
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}:{entry}</li>'
        content += '</ol>'
        send_email(to, subject, content)
        return super().form_valid(form)

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'

    

# Create your views here.
