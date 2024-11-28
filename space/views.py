from django.shortcuts import render
from .models import SliderImage


def slider_view(request):
    slider_images = SliderImage.objects.all()
    return render(request, 'space/index.html', {'slider_images': slider_images})
