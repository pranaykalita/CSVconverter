from django.contrib import admin
from .models import UploadHistory

# Register your models here.
@admin.register(UploadHistory)
class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("id", "file_name","converted_type","timestamp")
