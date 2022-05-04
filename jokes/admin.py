from django.contrib import admin
from .models import Category, Tag, Joke, JokeVote

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated'] 

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['tag', 'created', 'updated'] 

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Joke)
class Joke(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'answer', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: #editing an existint object
            return ('slug', 'created', 'updated')
        
        return ()

@admin.register(JokeVote)
class JokeVote(admin.ModelAdmin):
    model = JokeVote
    list_display = ['joke', 'user', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: #editing an existint object
            return ('slug', 'created', 'updated')
        
        return ()
# Register your models here.
