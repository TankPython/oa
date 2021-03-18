from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from role import views

urlpatterns = [
    path('role/', views.RoleView.as_view()),
    path('user/', views.UserView.as_view()),
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('menu/', views.MenuView.as_view()),
    path('right/', views.RightView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

