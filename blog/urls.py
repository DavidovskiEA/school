from django.urls import path

from .views import *


app_name = 'SChool'

urlpatterns = [
    path('school/all', SchoolCreateView.as_view()),
    path('group/all', GroupCreateView.as_view()),
    path('student/all', StudentCreateView.as_view()),

]