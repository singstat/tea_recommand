from django.shortcuts import render
from django.utils import timezone
from .models import Entry
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404

from .forms import PostForm

def tea_list(request):
    posts = Entry.objects.order_by('-created_date')
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render('tea_log/tea_list.html', {'posts': posts, 'form': form})
    else:
        form = PostForm()
            
    return render(request, 'tea_log/tea_list.html', {'posts': posts, 'form': form})

def user_detail(request, un):
    post = Entry.objects.filter( author= User.objects.get(username= un).pk ).order_by('-created_date')
    return render(request, 'tea_log/user_detail.html', {'posts': post,'name': un})

def log_new(request):
    form = PostForm()
    return render(request, 'tea_log/log_edit.html', {'form': form})
# Create your views here.
