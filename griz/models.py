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


class Dog(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        db_index=True,
    )
    def __str__(self):
        if self.name and self.breed:
            return f"{self.name} ({self.breed})"
        return self.name or "Unnamed dog"


class Entry(models.Model):
    dog = models.ForeignKey(
        Dog,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="entries",
    )

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

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.dog and self.date:
            return f"Entry for {self.dog} on {self.date}"
        return f"Entry {self.pk}"

