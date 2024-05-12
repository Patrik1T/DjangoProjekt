from django.shortcuts import render
from .models import otazkakmaturite

def index(request):
    context = {
        'otazkakmaturite': otazkakmaturite.objects.order_by('-rate').all()[:3],
    }
    return render(request, 'index.html', context=context)
