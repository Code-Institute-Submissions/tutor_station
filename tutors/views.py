from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Tutor, Subject
from .forms import TutorForm


def all_tutors(request):
    """ A view to show all tutorss, including sorting and search queries """

    tutors = Tutor.objects.all()
    query = None
    subjects = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tutors = tutors.annotate(lower_name=Lower('name'))
            if sortkey == 'subject':
                sortkey = 'subject__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tutors = tutors.order_by(sortkey)

        if 'subject' in request.GET:
            subjects = request.GET['subject'].split(',')
            tutors = tutors.filter(subject__name__in=subjects)
            subjects = subjects.objects.filter(name__in=subjects)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('tutors'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tutors = tutors.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tutors': tutors,
        'search_term': query,
        'current_subjects': subjects,
        'current_sorting': current_sorting,
    }

    return render(request, 'tutors/tutors.html', context)


def tutor_detail(request, tutor_id):
    """ A view to show individual tutor details """

    tutor = get_object_or_404(Tutor, pk=tutor_id)

    context = {
        'tutor': tutor,
    }

    return render(request, 'tutors/tutor_detail.html', context)


@login_required
def add_tutor(request):
    """ Add a tutor to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES)
        if form.is_valid():
            tutor = form.save()
            messages.success(request, 'Successfully added Tutor!')
            return redirect(reverse('tutor_detail', args=[tutor.id]))
        else:
            messages.error(request, 'Failed to add tutor. Please ensure the form is valid.')
    else:
        form = TutorForm()

    template = 'tutors/add_tutor.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tutor(request, tutor_id):
    """ Edit a tutor in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    tutor = get_object_or_404(Tutor, pk=tutor_id)
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES, instance=tutor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Tutor!')
            return redirect(reverse('tutor_detail', args=[tutor.id]))
        else:
            messages.error(request, 'Failed to update tutor. Please ensure the form is valid.')
    else:
        form = TutorForm(instance=tutor)
        messages.info(request, f'You are editing {tutor.name}')

    template = 'tutorss/edit_tutor.html'
    context = {
        'form': form,
        'tutor': tutor,
    }

    return render(request, template, context)


@login_required
def delete_tutor(request, tutor_id):
    """ Delete a Tutor from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    tutor = get_object_or_404(Tutor, pk=tutor_id)
    tutor.delete()
    messages.success(request, 'Tutor deleted!')
    return redirect(reverse('tutors'))
