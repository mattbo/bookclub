from django import template
from django.utils.safestring import mark_safe
from django.forms.forms import BaseForm #for comparison

register = template.Library()

@register.filter
def latest_comment(book, comments):
    '''assumes comments are sorted chronologically'''
    for comment in comments.all():
        print("Got a comment, book is {0}(id {2}, page is {1}".format(
            comment.book, comment.page, comment.book.id))
        print("Input book is {0} (id {1})".format(book, book.id))
        if book.id == comment.book.id:
            return "You're on page {0}.".format(comment.page)
    return ""

@register.filter
def index_list(lst, idx):
    '''Stupid cheat to use a forloop counter to index an object'''
    html = ''
    obj = lst[idx]
    if issubclass(type(obj), BaseForm):
        html += obj.non_field_errors().as_ul()
        html += '<table>'
        html += obj.as_table()
        html += '</table>'
    else : html = str(obj)
    return mark_safe(html)
