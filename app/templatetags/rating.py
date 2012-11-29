from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)


@register.filter(name='subtract')
def subtract(first, second):
    return first - second


@register.filter(name='absolute')
def absolute(num):
    return abs(num)
