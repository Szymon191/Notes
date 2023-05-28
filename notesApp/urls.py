from django.http import HttpResponseNotFound
from django.urls import path, re_path
from notesApp import views
from notesApp.views import index, categorie, add, edit, DeleteTask

app_name = 'notesApp'

def disable_favicon(request):
    return HttpResponseNotFound()


urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>', edit.as_view(), name='edit'),
    path('add/', add, name='add'),
    path('del/<int:pk>', DeleteTask.as_view(), name='delete'),
    path('<str:categ>/', categorie, name='categorie'),
    re_path(r'^favicon\.ico$', disable_favicon),
]