from django.urls import path
from apps.Auto.views import upload_car_data_from_json_file

urlpatterns = [
    path('upload/', upload_car_data_from_json_file, name='car_upload'),
]
