from django import template

register = template.Library()

@register.filter
def rang(n):
    
    return range(n)