from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import *
from django.utils import timezone

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def show_popular(request):
	return render(request, 'qa/question_list.html')

def show_new(request):
	return render(request, 'qa/question_list.html')

def show_question(request, pk):
	return render(request, 'qa/question.html', {'pk': pk})

def ask_question(request):
	form = QuestionForm(request.POST)
	if form.is_valid():
		question = form.save(commit=False)
		question.added_at = timezone.now()
		question.rating = 0		
		question.save()
		return redirect('qa/show_question.html', pk=question.pk)
	else:
	 	form = QuestionForm()
	return render(request, 'qa/question_edit.html', {'form': form})




