from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .forms import PatientForm
from .models import Patient


def new_patient(request):
    if request.method == "POST":
        filled_form = PatientForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "New patient record has been added."
            new_form = PatientForm()

            return render(request, "patients/patient_form.html", {"note": note, "patient_form": new_form})
    else:
        form = PatientForm()

        return render(request, "patients/patient_form.html", {"patient_form": form})


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"


class PatientDetailView(DetailView):
    model = Patient


def update_view(request, pk):
    obj = get_object_or_404(Patient, id=pk)
    form = PatientForm(instance=obj)
    if request.method == "POST":
        filled_form = PatientForm(request.POST, instance=obj)
        if filled_form.is_valid():
            filled_form.save()

            return HttpResponseRedirect("/patients/records/" + str(pk))
    else:

        return render(request, "patients/patient_form.html", {"patient_form": form})


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = "/patients/records"
