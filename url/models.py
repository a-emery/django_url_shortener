from django.db import models
from django.utils.crypto import get_random_string


def random_string():
    return get_random_string(length=8)


class Bookmark(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    endpoint = models.URLField()
    user = models.CharField(max_length=255)
    short_name = models.CharField(max_length=8, default=random_string())
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True, blank=True, null=True)
