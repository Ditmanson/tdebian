from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry, Tag, Dog
from django.utils.dateparse import parse_date
# from .forms import EntryFilterForm


def grizIndex(request):
    entries = Entry.objects.all().order_by('-date')[:3]  # newest first
    tags = Tag.objects.all()
    # dogs = Dog.objects.all()
    context = {
        'entries': entries,
        'tags': tags,
        # 'dogs': dogs,
        # 'form': EntryFilterForm(),
    }
    return render(request, 'grizIndex.html', context)

def grizContent(request):
    entries = Entry.objects.all().order_by('-date')  # newest first
    tags = Tag.objects.all()
    context = {
        'entries': entries,
        'tags': tags,
    }
    return render(request, 'grizContent.html', context)

def grizTag(request, myTag ):
    entries = Entry.objects.filter(tags__name=myTag).order_by('-date')  # newest first
    context = {
        'entries': entries,
    }
    return render(request, 'grizContent.html', context)

# def grizDateRange(request):
#     """
#     Filter entries by start and end date (inclusive)
#     GET parameters: start_date=YYYY-MM-DD, end_date=YYYY-MM-DD
#     """
#     # entries = Entry.objects.all().order_by('-date')
#     entries = Entry.objects.exclude(date__isnull=True).order_by('-date')
#
#     start_str = request.GET.get('start_date')
#     end_str = request.GET.get('end_date')
#
#     if start_str:
#         start_date = parse_date(start_str)
#         if start_date:
#             entries = entries.filter(date__gte=start_date)
#
#     if end_str:
#         end_date = parse_date(end_str)
#         if end_date:
#             entries = entries.filter(date__lte=end_date)
#
#     context = {
#         'entries': entries,
#     }
#     return render(request, 'grizContent.html', context)
