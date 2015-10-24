from django.shortcuts import render
from django.utils import timezone
from .models import Entry
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404

from .forms import PostForm, TeaInfo, TeaForm


from django.contrib.auth.decorators import login_required

def tea_list(request):
    posts = Entry.objects.order_by('-created_date')
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.published_date = timezone.now()
            post.save()
            post.author = request.user
#			if request.user.is_authenticated():
#				post.author = request.user
#			else:
#				post.author = User.objects.get(username= 'sing')

            return render(request,'tea_log/tea_list.html', {'posts': posts, 'form': form})
    else:
        form = PostForm()

    return render(request, 'tea_log/tea_list.html', {'posts': posts, 'form': form})


def user_detail(request, un):
    post = Entry.objects.filter( author= User.objects.get(username= un).pk ).order_by('-created_date')
    return render(request, 'tea_log/user_detail.html', {'posts': post,'name': un})

@login_required(login_url='/accounts/login/')
def add_new(request):
    form = TeaInfo()
    if request.method == "POST":
        form = TeaInfo(request.POST)
        if form.is_valid():
            form.save()
            form = TeaInfo()
            return render(request, 'tea_log/edit.html', {'form': form})
    else:
        form = TeaInfo()
    return render(request, 'tea_log/edit.html', {'form': form})

@login_required(login_url='/accounts/login/')	
def add_tea(request):
    form = TeaForm()
    if request.method == "POST":
        form = TeaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'tea_log/edit2.html', {'form': form})
    else:
        form = TeaForm()

    return render(request, 'tea_log/edit2.html', {'form': form})

#def add_two(request):
#	form = TeaInfo()
#	sub_form = TeaForm()
#	if request.method == "POST":
#		form = TeaInfo(request.POST)
#		sub_form = TeaForm(request.POST)
#		if form.is_valid():
#			form.save()
#			form = TeaInfo()
#			return render(request, 'tea_log/edit.html', {'form': form, 'sub_form': sub_form})
#		if sub_form.is_valid():
#			post = sub_form.save(commit=False)
#			post.author = request.user
#			post.published_date = timezone.now()
#			post.save()
#	else:
#		form = TeaInfo()
#		sub_form = TeaForm()
#	return render(request, 'tea_log/edit.html', {'form': form, 'sub_form':sub_form})
# Create your views here.
