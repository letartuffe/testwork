#-*- coding: utf-8 -*-
from testwork.quiz.models import *
from django.contrib import admin

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class chaptersAdmin(admin.ModelAdmin):
    list_display = ('title',)

class casesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)

class titlesQuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)

class tagsQuizAdmin(admin.ModelAdmin):
    list_display = ('title',)

class QuizzesAdmin(admin.ModelAdmin):
    list_display = ('titleQuiz',)
#    fieldsets = [ ('과목', {'fields': ['subject']}),
#    ('단위', {'fields': ['chapter']})]

admin.site.register(subjectsQuiz, SubjectsAdmin)
admin.site.register(chaptersQuiz, chaptersAdmin)
admin.site.register(casesQuiz, casesAdmin)
admin.site.register(titlesQuiz, titlesQuizAdmin)
admin.site.register(tagsQuiz, tagsQuizAdmin)


admin.site.register(quizzes, QuizzesAdmin)
