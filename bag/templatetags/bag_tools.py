from django import template
from decimal import Decimal


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_vat')
def calc_vat(price, quantity):
    return (price * quantity) * Decimal(0.25)
