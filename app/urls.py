from django.urls import path
from . import views

urlpatterns = [
    path('',             views.login_view,    name='login'),
    path('logout/',      views.logout_view,   name='logout'),
    path('dashboard/',   views.dashboard,     name='dashboard'),
    path('add/',         views.add_student,   name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
