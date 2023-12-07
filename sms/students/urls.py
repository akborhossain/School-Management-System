from django.urls import path
from .views import AdmissionView, AdmissionSuccessView
urlpatterns = [
    path('admission/', AdmissionView.as_view(),name='admission'),
    path('dept/', AdmissionSuccessView.as_view(), name='admission_success'),
]