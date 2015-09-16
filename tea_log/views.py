from django.shortcuts import render
from django.utils import timezone
from .models import Entry

def tea_list(request):
    posts = Entry.objects.order_by('-created_date')
    
    return render(request, 'tea_log/tea_list.html', {'posts': posts})
# Create your views here.
