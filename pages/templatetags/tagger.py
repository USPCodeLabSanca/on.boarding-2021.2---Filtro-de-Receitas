from django import template

register = template.Library()

@register.filter(name='private')
def private(obj, attribute):
    return getattr(obj, attribute)

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value