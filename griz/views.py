from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(request):
    entries = Entry.objects.all().order_by('-date')  # newest first
    context = {
        'entries': entries,
    }
    return render(request, 'index.html', context)


#def index(request):
#    return HttpResponse("Hello world")
