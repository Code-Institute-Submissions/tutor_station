from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Tutor


def profile_security(request):

    if request.user.is_authenticated:

        tutorget = Tutor.objects.filter(user=request.user)
        if len(tutorget) > 0:
            tutor_user = tutorget.values_list('user', flat=True)[0]
            tutor_id = tutorget.values_list('id', flat=True)[0]

            context = {
                'tutorget': tutorget,
                'tutorcount': len(tutorget),
                'tutor_user': tutor_user,
                'tutor_id': tutor_id,
            }
        else:
            context = {
                'tutorget': 0,
                'tutorcount': 0,
                'tutor_user': '',
                'tutor_id': 0,
            }
    else:
        context = {
            'tutorget': 0,
            'tutorcount': 0,
            'tutor_user': '',
            'tutor_id': 0,
        }

    return context
