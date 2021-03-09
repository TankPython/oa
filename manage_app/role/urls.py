from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from role import views

urlpatterns = [
    path('roles/', views.RoleViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
