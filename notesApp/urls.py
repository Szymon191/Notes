from django.urls import path
from notesApp import views
from notesApp.views import index, categorie, add, edit

app_name = 'notesApp'

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>', edit.as_view(), name='edit'),
    path('add/', add, name='add'),
    path('<str:categ>/', categorie, name='categorie'),
]