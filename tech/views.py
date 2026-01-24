from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry, Tag

def techIndex(request):
    entries = Entry.objects.all().order_by('-date')  # newest first
    tags = Tag.objects.all()
    context = {
        'entries': entries,
        'tags': tags,
    }
    return render(request, 'techIndex.html', context)

def techContent(request):
    entries = Entry.objects.all().order_by('-date')  # newest first
    tags = Tag.objects.all()
    context = {
        'entries': entries,
        'tags': tags,
    }
    return render(request, 'techContent.html', context)

def techTag(request, myTag ):
    entries = Entry.objects.filter(tags__name=myTag).order_by('-date')  # newest first
    context = {
        'entries': entries,
    }
    return render(request, 'techContent.html', context)
