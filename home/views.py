from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
