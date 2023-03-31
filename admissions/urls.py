from django.urls import path
from admissions.views import addAdmission
from admissions.views import admissionsReport
from admissions.views import addVendor
from admissions.views import deleteStudent
from admissions.views import updateStudent
from .views import upload_image  # image and date
from admissions.views import calculate_bmi
from admissions import views

urlpatterns = [

    path('newadm/', addAdmission),
    path('admreport/', admissionsReport),
    path('newVendor/', addVendor),
    path('delete/<int:id>/', deleteStudent),
    path('update/<int:id>/', updateStudent),
    path('bmi/', calculate_bmi, name='calculate_bmi'),
    path('upload-image/', upload_image, name='upload_image'),  # date and image

]
