from django.db import models

from apps.common.models import BaseModel


class Paymet(BaseModel):
	title = models.CharField(max_length=255, default='')

