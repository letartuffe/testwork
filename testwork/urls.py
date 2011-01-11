#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()
import os.path

media = os.path.join(os.path.dirname(__file__), 'media')
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testwork/', include('testwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^quiz/list$', 'testwork.quiz.views.quizList'),
    (r'^quiz/scoring$', 'testwork.quiz.views.scoring'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media}),
    #카운터
    (r'^count/', include('django_counter.urls')),
)
