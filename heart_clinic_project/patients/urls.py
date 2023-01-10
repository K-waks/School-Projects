from django.urls import path
from . import views

urlpatterns = [
    path("records/new", views.new_patient, name="PatientCreateView"),
    path("records", views.PatientListView.as_view(), name="PatientListView"),
    path("records/<int:pk>", views.PatientDetailView.as_view(), name="PatientDetailView"),
    path("records/<int:pk>/edit", views.update_view, name="PatientUpdateView"),
    path("records/<int:pk>/delete", views.PatientDeleteView.as_view(), name="PatientDeleteView"),
]
