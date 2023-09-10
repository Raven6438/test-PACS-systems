from django.urls import path
from . import views

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path('studies/', views.StudiesView.as_view(), name='get_studies'),
]