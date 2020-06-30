from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tutors, name='tutors'),
    path('<int:tutor_id>/', views.tutor_detail, name='tutor_detail'),
    path('add_tutor/', views.add_tutor, name='add_tutor'),
    path('edit/<int:tutor_id>/', views.edit_tutor, name='edit_tutor'),
    path('delete/<int:tutor_id>/', views.delete_tutor, name='delete_tutor'),
]
