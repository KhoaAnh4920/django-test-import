# resources.py
from import_export import resources
from member.models import Member
from django.http import HttpResponse
import csv
from rest_framework import exceptions


class MemberResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        parent_id = row['parent']
        # if parent_id is not None:
        parent = Member.objects.filter(pk=parent_id).first()
        # if parent:
        row['parent'] = parent
        # next

    def skip_row(self, instance, original, row, import_validation_errors=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"'
        check = []
        new = Member.objects.all()
        for p in new:
            check.append(p.email)
        # if instance.email in check:
        #     print(f'Skipped {row}')
        #     return True
        # else:
        #     print(f'Imported {row}')
        #     return False
        parent_id = row['parent']
        # parent is not NULL
        if parent_id is not None:
            parent = Member.objects.filter(pk=parent_id).first()
            # Member not exist or email already exist
            if not parent or instance.email in check:
                print(f'Skipped {row}')
                return True
            else:
                print(f'Imported {row}')
                row['parent'] = parent
                return False
        else:
            if instance.email in check:
                print(f'Skipped {row}')
                row['parent'] = None
                return True
            else:
                print(f'Imported {row}')
                row['parent'] = None
                return False

    class Meta:
        model = Member
