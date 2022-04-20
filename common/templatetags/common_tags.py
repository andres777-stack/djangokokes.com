import random 
from django import template
from jokes.models import Joke

register = template.Library()

@register.inclusion_tag('common/joke.html')
def random_joke():
    count = Joke.objects.count()
    if count > 0:
        i = random.randint(0, count-1)
        print(i)
        joke = Joke.objects.all()[i]
        print(joke)
        return {'joke': joke} 
    else:
        return {'joke':{
            'question': 'You know what is funny?',
            'answer': 'There are no joke in the database.'
        }
        }