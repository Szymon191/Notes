from django.contrib import admin

from notesApp.models import Categorie, Note


# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'bg_color')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'body', 'categorie')