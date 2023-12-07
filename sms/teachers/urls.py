from django.urls import path
from .views import CreateTeacher

urlpatterns = [
    path('create/',CreateTeacher.as_view(),name='createteacher'),
]