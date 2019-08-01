from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from tipdaily.version1.models import Person
# from .models import Person
# from version1.models import Person


def hello(response):
    return HttpResponse('<h1>Hello Animalworld!</h1>')


def home(response):
    return HttpResponse('<h1>Welcome to Python Tips! </h1> <i> ... curated by Obafemi<i><br><a href="/pythontips">View Tips</a>')


# def contact_list(request):
#     persons = Person.objects.all().order_by('first_name')
#     return render(request, 'version1/contact_list.html', {'persons': persons})