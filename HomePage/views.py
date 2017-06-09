from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os

def homepage(request):
    return render(request, 'HomePage/HP_v1.html')

def show_image(request, *args, **kwargs):
	name1 = request.GET['name'] + '.jpg'
	print(name1)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	image=BASE_DIR + '/HomePage/images/' + name1
	file = Image.open(image)
	print(image)
	response = HttpResponse(file, content_type='image/jpg', status=200)
	response['Content-Disposition'] = 'attachment; filename=%s.jpg' % name1
	return response

