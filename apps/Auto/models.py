from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class Auto(BaseModel):
    title = models.CharField(max_length=255, null=True)
    is_publish = models.BooleanField(default=False)
    total_views = models.PositiveIntegerField(default=0)