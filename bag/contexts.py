from decimal import Decimal
from django.shortcuts import get_object_or_404
from tutors.models import Tutor


def bag_contents(request):

    bag_items = []
    total = 0
    tutor_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        tutor = get_object_or_404(Tutor, pk=item_id)
        total += item_data * tutor.krona_per_hour
        tutor_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'tutor': tutor,
        })

    vat = total * Decimal(0.25)
    total = total - vat
    grand_total = total + vat

    context = {
        'bag_items': bag_items,
        'total': total,
        'tutor_count': tutor_count,
        'vat': vat,
        'grand_total': grand_total,
    }

    return context
