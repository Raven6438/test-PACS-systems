from django.urls import path
from . import views

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path('patients/', views.StudiesView.as_view(), name='get_studies'),
]