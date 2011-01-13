#-*- coding: utf-8 -*-

# Create your views here.
from testwork.quiz.models import casesQuiz, chaptersQuiz, quizzes, subjectsQuiz, tagsQuiz, titlesQuiz

from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response #shortcut
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
#from django.core.paginator import Paginator, InvalidPage, EmptyPage #페이징


def underline(a):
    targetInner = []
    for quiz in a:
        if quiz.case.id == 3 :
            targetInner.append(quiz.firstAnswer)
            targetInner.append(quiz.secondAnswer)
            targetInner.append(quiz.thirdAnswer)
            targetInner.append(quiz.fourthAnswer)
            if quiz.fifthAnswer :
                targetInner.append(quiz.fifthAnswer)
            quiz.allAnswer = targetInner
    return a

def quizList(request):
    a = underline(get_list_or_404(quizzes, is_public = True))
    #a = underline(get_list_or_404(quizzes.objects.filter(id__in = [6, 7, 8]), is_public = True))
    return render_to_response('list.html', {"a": a, }, context_instance = RequestContext(request))


def scoring(request):

    if request.method == 'POST':

        #총 몇문제
        #몇 문제 맞음 / 몇 문제 틀림
        #얼마의 시간동안
        #틀린문제는 - 정답과 틀린거 보여주기.


        scoringSource = request.POST.copy()
        del scoringSource['csrfmiddlewaretoken']


        #return HttpResponse("%s 번 맞음" % rightCheck)
        quizResultListNormal = get_list_or_404(quizzes.objects.filter(id__in = scoringSource))
        quizResultListNormal = underline(quizResultListNormal)

        basket = []#답반따로 보내기 [정답,체크한답,그냥]
        rightCheck = 0 #맞은 개수
        for quiz in quizResultListNormal:

            if quiz.answerQuiz == scoringSource[str(quiz.id)]:
                rightCheck = rightCheck + 1
                quiz.is_right = True
            basket.append(quiz.answerQuiz)
            basket.append(scoringSource[str(quiz.id)])
            basket.append(quiz.is_right)
            quiz.scoreAnswer = basket
            basket = []


        num = []  #문제수, 맞은개수, 틀린개수
        num.append(len(scoringSource))





        num.append(rightCheck)
        num.append(num[0] - num[1])
        mode = 'score'
        return render_to_response('list.html', {"quizResultListNormal": quizResultListNormal, "mode":mode, "num":num, "scoringSource":scoringSource, }, context_instance = RequestContext(request))

        '''
        for k in scoringSource:
            if scoringSource[k] == quizzes.objects.values('answerQuiz').get(id = k).values()[0]:
                rightCheck.append(k)
        '''
def testhtml(request):
    a = ''
    return render_to_response('testhtml.html', {"a": a, }, context_instance = RequestContext(request))
    
    