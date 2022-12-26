from django.urls import path
from member import views


urlpatterns = [
    # get list create product with out variant for admin
    path('test-import/', views.import_data,
         name='test-import-aa'),
    #     path('test-import-2/', views.simple_upload,
    #          name='test-import-bb'),
]
