from django.contrib import admin
from .models import Tag, Dog, Entry


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "breed", "birthday")


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("dog", "date", "youtube_url", "created_at", "youtube_embed")
    list_filter = ("tags", "date", "dog")
    search_fields = ("text", "dog__name", "tags__name")


# Register your models here.
