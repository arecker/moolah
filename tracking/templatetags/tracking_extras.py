from django import template
import locale
locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.filter()
def currency(value):
    try:
        return locale.currency(value, grouping=True)
    except TypeError:
        return '$0.00'
