from django.db import models
from datetime import datetime


class Document(models.Model):
    docfile = models.FileField(upload_to='media/')
    date_upload = models.DateTimeField(default=datetime.now, blank=True)
