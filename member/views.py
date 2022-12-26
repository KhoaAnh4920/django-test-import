from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse
from member.resources import MemberResource
from tablib import Dataset
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def import_data(request):
    print('BBB')
    if request.method == 'POST':
        print('AAA')
        file_format = request.POST['file-format']
        employee_resource = MemberResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        # test = new_employees.name
        # print('Format: ', new_employees.name)

        # if test.endswith('.csv'):
        #     print('OK !!')

        if file_format == 'CSV':
            # print("DDD")
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='csv')
            result = employee_resource.import_data(
                dataset, dry_run=True, raise_errors=True)
            # print("End: ", result)
        elif file_format == 'JSON':
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)
        elif file_format == 'XLSX':
            print("Run excel")
            # Testing data import
            imported_data = dataset.load(new_employees.read(), format='xlsx')
            result = employee_resource.import_data(
                dataset, dry_run=True, raise_errors=True)

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return HttpResponse({'OK'}, content_type='application/json')


# @csrf_exempt
# def simple_upload(request):
#     print("Simple 2")
#     if request.method == 'POST':
#         person_resource = MemberResource()
#         dataset = Dataset()
#         new_persons = request.FILES['myfile']
#         print("new_persons: ", new_persons)
#         imported_data = dataset.load(new_persons.read())
#         print("imported_data: ", imported_data)
#         result = person_resource.import_data(
#             dataset, dry_run=True)  # Test the data import

#         if not result.has_errors():
#             person_resource.import_data(
#                 dataset, dry_run=False)  # Actually import now
#     return HttpResponse({'OK'}, content_type='application/json')
