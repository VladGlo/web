import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *


def lab7(request):
    text = request.POST.get('input_text')

    search_id = request.POST.get('textfield', None)
    template = loader.get_template('lab7.html')
    context = {}
    if request.method == 'POST':
        if text == "длинный":
            context = {'rows_var': "40", 'cols_var': "30", 'text': text}
        elif text == "широкий":
            context = {'rows_var': "10", 'cols_var': "60", 'text': text}
        elif text == "большой":
            context = {'rows_var': "40", 'cols_var': "60", 'text': text}
        elif text == "маленький":
            context = {'rows_var': "5", 'cols_var': "15", 'text': text}
        else:
            context = {'text': text}
    return HttpResponse(template.render(context, request))


def lab8(request):
    queryset = ExamMarks.objects.order_by('exam_id').values('mark', 'exam_id', 'stud_id', 'subj_id', 'exam_date').distinct()
    for item in queryset:
        print(item)
    template = loader.get_template('lab8.html')
    return HttpResponse(template.render({'exam_list': queryset}, request))


def lab9(request):
    max_hours = Subject.objects.order_by('-hour')[0]
    print(max_hours.hour)
    queryset = Subject.objects.filter(hour=max_hours.hour)
    for item in queryset:
        print(item)
    template = loader.get_template('lab9.html')
    return HttpResponse(template.render({'subj_list': queryset}, request))
