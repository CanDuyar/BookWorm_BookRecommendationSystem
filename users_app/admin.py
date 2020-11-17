from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User


@admin.register(User)
class UserDetail(ImportExportModelAdmin):
    pass
