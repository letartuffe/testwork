#-*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django.utils.html import escape
from django import template
#from django.core.paginator import Paginator, InvalidPage, EmptyPage #페이징


register = template.Library()

@register.filter
def highlight(text, word1):
    for n in word1:
        text = mark_safe(text.replace(n, "<u>%s</u>" % n))
    return text


@register.filter
def checkedF(a, b):
    #b = [정답, 체크한답, is_right]
    if not b[2] and  int(a) == int(b[1]):
        return mark_safe('class="red"')
    elif not b[2] and int(a) == int(b[0]):
        return mark_safe('class = "blue"')
    elif b[2] and int(a) == int(b[0]):
        return mark_safe('class = "blue"')
    else:
        return ''

@register.filter
def countQuiz(a, b):
    return "총 %s문제 중 %s문제 맞고 %s문제 틀림" % (str(b[0]), str(b[1]), str(b[2]))
