from django.shortcuts import render

# Create your views here.


def top(request):
    context = {}
    return render(request, 'top.html', context)
