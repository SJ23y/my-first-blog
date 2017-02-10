from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def show_main(request):
    return render(request, 'qa/mainqa.html')
