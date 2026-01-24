from django.db import models

class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
    )

    def __str__(self):
        return self.name or "Unnamed tag"


class Entry(models.Model):
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="entries",
    )

    date = models.DateField(
        null=True,
        blank=True,
        db_index=True,
    )

    youtube_url = models.URLField(
        null=True,
        blank=True,
    )
    youtube_embed = models.URLField(
        null=True,
        blank=True,
    )

    text = models.TextField(
        null=True,
        blank=True,
    )

