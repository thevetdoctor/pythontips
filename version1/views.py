# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Person

# Create your views here.

def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'contact_list.html', {'persons': persons})


def contact_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonForm()
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/person/' + str(person.pk))
    else:
        form = PersonForm(instance=person)
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('/')