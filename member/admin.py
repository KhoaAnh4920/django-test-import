from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from member.models import Member
from member.resources import MemberResource


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ("firstname", "lastname", "email", "birth_date")

    # def get_confirm_form_initial(self, request, import_form):
    #     initial = super().get_confirm_form_initial(request, import_form)
    #     # Pass on the `author` value from the import form to
    #     # the confirm form (if provided)
    #     print("Run confirm")
    #     # if import_form:
    #     #     print('Test: ', import_form.cleaned_data['firstname'])
    #     # return initial
