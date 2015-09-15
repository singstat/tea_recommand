from django.shortcuts import render
from django.utils import timezone
from .models import Log_structure

def tea_list(request):
    posts = Log_structure.objects.order_by('-published_date')
    
    return render(request, 'tea_log/tea_list.html', {'posts': posts})
# Create your views here.
