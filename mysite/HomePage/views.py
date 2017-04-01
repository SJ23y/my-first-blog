from django.shortcuts import render


def homepage(request):
    return render(request, 'HomePage/HP_v1.html')
