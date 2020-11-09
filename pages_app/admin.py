from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import BookClass


@admin.register(BookClass)
class BookDetail(ImportExportModelAdmin):
    pass
