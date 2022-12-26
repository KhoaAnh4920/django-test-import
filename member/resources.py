# resources.py
from import_export import resources
from member.models import Member
from django.http import HttpResponse
import csv


class MemberResource(resources.ModelResource):

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     print("Run before_import !!")

    def before_import_row(self, row, **kwargs):
        # print("Run this !!!")
        # print('row parent: ', row['parent'])
        parent = Member.objects.get(pk=row['parent'])
        # print('parent: ', parent)
        row['parent'] = parent
        # next

    def skip_row(self, instance, original, row, import_validation_errors=None):
        print('Row: ', row)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"'
        check = []
        new = Member.objects.all()
        for p in new:
            check.append(p.email)
        if instance.email in check:
            print('True')
            writer = csv.writer(response)
            writer.writerow([instance.id, instance.email, instance.firstname])
            return response
        else:
            print("no")
            return False

    class Meta:
        model = Member
