from django.shortcuts import render
from django.utils import timezone
from .models import Entry
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404

def tea_list(request):
    posts = Entry.objects.order_by('-created_date')
    
    return render(request, 'tea_log/tea_list.html', {'posts': posts})

def user_detail(request, un):
    post = Entry.objects.filter( author= User.objects.get(username= un).pk )
    return render(request, 'tea_log/tea_list.html', {'posts': post})
# Create your views here.
