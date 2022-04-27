from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Joke
from django.urls import reverse_lazy
from .forms import JokeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

#This view is for created a new object
class JokeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_messssage = 'Joke created.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke update'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
# Create your views here.
