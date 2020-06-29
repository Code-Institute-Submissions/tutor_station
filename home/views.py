from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

def index(request):
    """ A view to return the index page """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm()
    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)
