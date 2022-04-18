from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Joke

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

#This view is for created a new object
class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']
# Create your views here.
