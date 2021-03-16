from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hr_manage import views

urlpatterns = [
    path('client/', views.Client.as_view()),
    path('department/', views.Department.as_view()),
    path('Staff/', views.Staff.as_view()),
    path('Sign/', views.Sign.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
