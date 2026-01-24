from django.contrib import admin
from .models import Tag, Entry


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("date", "youtube_url",  "youtube_embed")
