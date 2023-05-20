from django.urls import path
from notesApp.views import index, categorie, add


app_name = 'notesApp'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('<str:categ>/', categorie, name='categorie'),
]