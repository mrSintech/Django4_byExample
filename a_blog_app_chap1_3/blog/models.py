from django.db import models
from django.utils import timezone


class Post(models.Model):

    # status choice
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'  # choice = respective val, readable val
        PUBLISHED = 'PB', 'Published'

    # We can access Post.Status.choices to obtain the available choices,
    # Post.Status.labels to obtain the human-readable names,
    # and Post.Status.values to obtain the actual values of the choices.

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)  # tz aware
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # by using auto_now the field will automatically update every time
    # the object update

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    # Blog posts by default displayed in reverse
    # chronological order (from newest to oldest) now we define a new ordering
    # for this model
    class Meta:
        ordering = ['-publish']
        # defining index for field will improve performance for queries
        # filtering or ordering results by this field
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
