from django.shortcuts import render, get_object_or_404
from datetime import timedelta, datetime

from django.views.decorators.csrf import csrf_exempt
from jsonview.decorators import json_view

from . models import Drawing


def draw(request):
    drawing = Drawing.objects.create(valid_to=datetime.now() + timedelta(seconds=20))
    return render(request, 'draw.html', {'token': drawing.token})


@csrf_exempt
@json_view
def update(request):
    if request.method == 'GET':
        print request.GET
        drawing = get_object_or_404(Drawing, token=request.GET.get('token', None))
        drawing.data = request.GET.get('data')
    else:
        print request.POST
        drawing = get_object_or_404(Drawing, token=request.POST.get('token', None))
        drawing.data = request.POST.get('data')

    drawing.save()

    # for r, g, b in zip(*[iter(drawing.data.split(","))] * 3):
    #     print p, r, g, b
    #     pixels[p] = (r, g, b)
    #     p += 1

    return {'success': True}