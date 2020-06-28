from django import template
register = template.Library()

@register.filter(is_safe=True)
def split(value):
    value=value.replace('[','')
    value=value.replace(']','')
    value=value.replace("'",'')
    value=value.split(',')
    return value
