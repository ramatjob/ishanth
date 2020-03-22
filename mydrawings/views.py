from django.shortcuts import render,get_object_or_404
from .models import DrawingPageInfo

# Create your views here.

def all_drawings(request):
    drawingPageInfo = DrawingPageInfo.objects.all()
    return render(request,'mydrawings/drawings.html',{'drawingPageInfo':drawingPageInfo})

def detail(request, drawing_id):
    drawing = get_object_or_404(DrawingPageInfo,pk=drawing_id)
    return render(request,'mydrawings/detail.html',{'drawing': drawing})

