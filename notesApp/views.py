from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from notesApp.forms import addForm
from django.urls import reverse
from notesApp.models import Note, Categorie
from django.views.generic import UpdateView, DeleteView


def index(request):
    notes = Note.noteManager.all()
    cate = Categorie.cateManager.all()

    paginator = Paginator(notes, 6)
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        if int(page) < 0:
            notes = paginator.page(1)
        else:
            notes = paginator.page(paginator.num_pages)

    return render(request, 'web/index.html', {'notes': notes, 'categoris': cate, 'cate_name': 'All notes', 'page': page})


def categorie(request, categ):
    notes = Note.noteManager.filter(categorie__title=categ)
    cate = Categorie.cateManager.all()

    return render(request, 'web/index.html', {'notes': notes, 'categoris': cate, 'cate_name': categ})


def add(request):
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = addForm()

    cate = Categorie.cateManager.all()

    return render(request, 'web/add.html', {'form': form, 'categoris': cate, 'cate_name': 'Add note'})


class edit(UpdateView):
    model = Note
    template_name = 'web/edit.html'
    fields = ['title', 'body', 'categorie']
    extra_context = {'categoris':  Categorie.cateManager.all(), 'cate_name': 'Edit note', 'onchange': 'change_color()'}

    def get_success_url(self):
        return reverse('notesApp:index')


class DeleteTask(DeleteView):
    model = Note
    template_name = 'web/del.html'

    extra_context = {'categoris': Categorie.cateManager.all()}

    def get_success_url(self):
        return reverse('notesApp:index')