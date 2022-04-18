from django.views.generic import ListView, DetailView
from .models import Joke

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke
    
# Create your views here.
