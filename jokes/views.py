from django.views.generic import ListView
from .models import Joke

class JokeListView(ListView):
    model = Joke
    

# Create your views here.
