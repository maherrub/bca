import os
from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    value = value.date()
    delta = value - date.today()

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
        ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days

@register.filter(name='get_due_date_color')
def get_due_date_color(value):
    value = value.date()
    delta = value - date.today()

    if delta.days < 1:
        return "#FF0000"
    elif delta.days <= 3:
        return "#FF7400"
    else:
        return "#00CC00"

@register.filter(name='ellipses')
def ellipses(value, arg):
    original_string = value
    max_length = arg

    if len(original_string) <= max_length:
        return original_string
    else:
        return original_string[:max_length] + "..."


@register.filter(name='print_file_content')
def print_file_content(f):
    f.open()
    myfile = f.read()
    f.close()
    try:
        return myfile

    except IOError:
        return ''

@register.filter(name='print_file_withlines')
def print_file_withlines(f, args):
    f.open()
    myfile = f.readlines()
    maxlines = len(myfile)
    newmax = maxlines 
    f.close()

    try:
        if not args >= maxlines:
            return myfile[args]

    except IOError:
        return ''
   


@register.filter(name='filesize')
def filesize(value):
    """Returns the filesize of the filename given in value"""
    return os.path.getsize(value)

@register.filter(name='split')
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)
