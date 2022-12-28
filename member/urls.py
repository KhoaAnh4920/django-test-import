from django.urls import path
from member import views


urlpatterns = [
    # get list create product with out variant for admin
    path('test-import/', views.import_data,
         name='test-import-aa'),
    path('test-import-2/', views.ImportCSVView.as_view(),
             name='test-import-2'),
]
