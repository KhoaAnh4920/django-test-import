from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
