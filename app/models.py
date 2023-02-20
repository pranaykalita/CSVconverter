from django.db import models

# Create your models here.

class UploadHistory(models.Model):
    file_name = models.CharField(max_length=255)
    converted_type = models.CharField(max_length=255,default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
