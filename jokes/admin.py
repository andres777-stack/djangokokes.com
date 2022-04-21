from django.contrib import admin
from .models import Joke

@admin.register(Joke)
class Joke(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'answer', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: #editing an existint object
            return ('created', 'updated')
        
        return ()
# Register your models here.
