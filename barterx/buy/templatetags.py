from django import template
register = template.Library()

@register.filter
def get_range(value, max_value):
    return range(1, max_value + 1)
