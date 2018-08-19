from __future__ import unicode_literals
from __future__ import absolute_import
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import QuizForm, QuestionForm
from main.models import Quiz


def quiz_crm(request, template_name='quiz_crm.html'):
    quiz = Quiz.objects.all()
    data = {}
    data['object_list'] = quiz
    return render(request, template_name, data)


def quiz_create(request, template_name='post_quiz.html'):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('quiz_crm')
    return render(request, template_name, {'form': form})


def quiz_update(request, pk, template_name='post_quiz.html'):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizForm(request.POST or None, instance=quiz)
    if form.is_valid():
        form.save()
        return redirect('quiz_crm')
    return render(request, template_name, {'form': form})


def question_create(request, template_name='post_question.html'):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('quiz_crm')
    return render(request, template_name, {'form': form})
