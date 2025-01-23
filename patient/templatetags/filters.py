from django import template
from datetime import timedelta

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    field.field.widget.attrs['class'] = css_class
    return field

@register.filter(name='add_date')
def add_date(date, days):
    try:
        return date + timedelta(days=int(days))
    except (TypeError, ValueError):
        return date 
