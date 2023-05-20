from django.shortcuts import render, redirect

from notesApp.forms import addForm
from notesApp.models import Note, Categorie


def index(request):
    notes = Note.noteManager.all()
    cate = Categorie.cateManager.all()

    return render(request, 'web/index.html', {'notes': notes, 'categoris': cate})


def categorie(request, categ):
    notes = Note.noteManager.filter(categorie__title=categ)
    cate = Categorie.cateManager.all()

    return render(request, 'web/index.html', {'notes': notes, 'categoris': cate})


def redict(param):
    pass


def add(request):
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = addForm()

    cate = Categorie.cateManager.all()

    return render(request, 'web/add.html', {'form': form, 'categoris': cate})