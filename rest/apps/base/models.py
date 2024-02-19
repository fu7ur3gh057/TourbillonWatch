from django.db import models
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class PKIDMixin(models.Model):
    pk_id = models.BigAutoField(
        primary_key=True, editable=False, verbose_name=_("Primary Key")
    )

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name=_("UUID")
    )

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create Date"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Last Update"))

    class Meta:
        abstract = True
