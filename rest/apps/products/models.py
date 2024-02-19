from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.base.models import TimeStampedMixin


class Product(TimeStampedMixin):
    # Content type fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Watch(models.Model):
    pass


class Bracelet(models.Model):
    pass
