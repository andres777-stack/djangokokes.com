from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Joke
from django.urls import reverse_lazy
from .forms import JokeForm

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

#This view is for created a new object
class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
# Create your views here.
