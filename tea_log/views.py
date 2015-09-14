from django.shortcuts import render

def tea_list(request):
    return render(request, 'tea_log/tea_list.html', {})
# Create your views here.
