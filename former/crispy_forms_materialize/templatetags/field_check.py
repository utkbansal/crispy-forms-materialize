from django import template
from django import forms

register = template.Library()


@register.filter
def is_textarea(field):
    return isinstance(field.field.widget, forms.Textarea)
