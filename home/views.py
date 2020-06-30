from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from tutors.models import Tutor

def index(request):
    """ A view to return the index page """
    tutorget = Tutor.objects.filter(user=request.user)
    tutor_id = tutorget.values_list('id', flat=True)[0]
    context = {
        'tutorcount': len(tutorget),
        'tutor_id': tutor_id,
    }

    return render(request, 'home/index.html', context)
