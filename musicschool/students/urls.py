from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('edit/<int:student_id>/', views.student_edit, name='student_edit'),
]