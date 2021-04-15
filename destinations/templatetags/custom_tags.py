from django import template 

register = template.Library() 

@register.filter
def to_str(value):
    """converts int to string"""
    return str(value-1)

@register.filter
def combine_str_id(value,prefix):
    return prefix+value
