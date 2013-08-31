from django import template
from django.utils.safestring import mark_safe
from django.forms.forms import BaseForm #for comparison
from bootstrap_toolkit.templatetags import bootstrap_toolkit

register = template.Library()

@register.filter
def latest_comment(comments):
    '''assumes comments are sorted chronologically'''
    page = -1
    for comment in comments:
        if comment.page > page:
            page = comment.page

    if page == -1 :
        return "You haven't started yet"
    return "You're on page {0}.".format(page)

@register.filter
def index_list(form, idx):
    '''Stupid cheat to use a forloop counter to index an object'''
    html = ''
    html += form.non_field_errors().as_ul()
    html += '<table>'
    html += bootstrap_toolkit.as_bootstrap(form)
    html += '</table>'
    return mark_safe(html)

@register.filter
def reading_status(reading_list, idx):
    if reading_list[idx].end_date:
        return "(due {0})".format(reading_list[idx].end_date)
    elif reading_list[idx].accepted:
        return "(accepted, unscheduled)"
    else:
        return "(proposed)"

