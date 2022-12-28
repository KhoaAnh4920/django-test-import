from rest_framework import generics, status
from django.http import HttpResponse
from member.resources import MemberResource
from tablib import Dataset
from django.views.decorators.csrf import csrf_exempt
from member.serializers import MemberSerializer
import csv
from rest_framework.response import Response
import pandas as pd
from member.models import Member


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
            print(imported_data)
            result = employee_resource.import_data(
                dataset, dry_run=True)
            # print("End: ", result.failed_dataset)
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

    return HttpResponse(content={'OK'}, content_type='application/json')

# def get_all_error(errors):
#     if errors:


class ImportCSVView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        file_format = request.POST['file-format']
        file = request.FILES['importData']
        if file_format == 'CSV':
            data = []
            error_list = []
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                id = int(row['id'])
                serializer = MemberSerializer(data=row)
                validation = serializer.is_valid()
                dict = serializer.data
                dict['id'] = id
                dict['errors'] = ''
                if not validation:
                    for key in serializer.errors.keys():
                        error = serializer.errors.get(key)[0]
                        error += MemberSerializer.validate_data(serializer.validated_data.get(
                            'email'), serializer.validated_data.get('parent'))
                        dict['errors'] += error
                        error_list.append(error)
                data.append(dict)
            if error_list:
                data_frame = pd.DataFrame.from_dict(data)
                data_frame.to_csv('test.csv', index=False)
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'Imported CSV'}, status=status.HTTP_200_OK)


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
