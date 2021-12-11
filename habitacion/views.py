from django.shortcuts import render
from .models import Habitacion


def home(request):
    habitacion = Habitacion.objects.all()

    context = {
        'habitacion': habitacion,
    }
    return render(request, 'habitacion.html', context)