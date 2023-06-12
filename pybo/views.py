from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

# 로컬서버 실행 : python manage.py runserver
#def index(request):
#    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)