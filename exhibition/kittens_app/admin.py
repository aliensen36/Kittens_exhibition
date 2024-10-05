from django.contrib import admin
from .models import Breed, Kitten

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'age', 'breed', 'owner', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('color', 'breed', 'age', 'created_at')
    raw_id_fields = ('owner',)
    ordering = ('-created_at',)
