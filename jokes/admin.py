from django.contrib import admin
from .models import Category, Joke

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated'] 

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


# Register your models here.
