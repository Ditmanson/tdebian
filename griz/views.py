from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def grizIndex(request):
    entries = Entry.objects.all().order_by('-date')  # newest first
    context = {
        'entries': entries,
    }
    return render(request, 'grizIndex.html', context)


#def index(request):
#    return HttpResponse("Hello world")
