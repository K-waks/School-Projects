from django import forms
from .models import Patient
import pickle
import numpy


class PatientForm(forms.ModelForm):

    sex = forms.ChoiceField(
        label="Gender",
        choices=[
            (None, "-------"),
            ("Male", "Male"),
            ("Female", "Female"),
        ],
    )
    cp = forms.ChoiceField(
        label="Chest Pain Type",
        choices=[
            (None, "-------"),
            ("Typical angina", "Typical angina"),
            ("Atypical angina", "Atypical angina"),
            ("Non-anginal pain", "Non-anginal pain"),
            ("Asymptomatic", "Asymptomatic"),
        ],
    )
    fbs = forms.ChoiceField(
        label="Fasting Blood Sugar",
        choices=[
            (None, "-------"),
            ("Greater than 120 mg/ml", "Greater than 120 mg/ml"),
            ("Lower than 120 mg/ml", "Lower than 120 mg/ml"),
        ],
    )
    restecg = forms.ChoiceField(
        label="Resting Electrocardiographic Results",
        choices=[
            (None, "-------"),
            ("Normal", "Normal"),
            ("ST-T wave abnormality", "ST-T wave abnormality"),
            ("Left ventricular hypertrophy", "Left ventricular hypertrophy"),
        ],
    )
    exang = forms.ChoiceField(
        label="Exercise Induced Angina",
        choices=[
            (None, "-------"),
            ("Yes", "Yes"),
            ("No", "No"),
        ],
    )
    slope = forms.ChoiceField(
        label="Slope",
        choices=[
            (None, "-------"),
            ("Upsloping", "Upsloping"),
            ("Flat", "Flat"),
            ("Downsloping", "Downsloping"),
        ],
    )
    ca = forms.ChoiceField(
        label="No. of flourosope major vessels",
        choices=[
            (None, "-------"),
            ("Zero", "Zero"),
            ("One", "One"),
            ("Two", "Two"),
            ("Three", "Three"),
        ],
    )
    thal = forms.ChoiceField(
        label="Thalassemia",
        choices=[
            (None, "-------"),
            ("Normal", "Normal"),
            ("Fixed Defect", "Fixed Defect"),
            ("Reversable Defect", "Reversable Defect"),
        ],
    )

    class Meta:
        model = Patient
        fields = (
            "first_name",
            "surname",
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal",
            "target",
        )
        labels = {
            "first_name": " First Name",
            "surname": "Surname",
            "age": "Age",
            "sex": "Gender",
            "cp": "Chest Pain Type",
            "trestbps": "Resting Blood Pressure",
            "chol": "Serum Cholestrol (mg/dl)",
            "fbs": "Fasting Blood Sugar (> 120 mg/dl)",
            "restecg": "Resting Electrocardiographic Results",
            "thalach": "Max Heart Rate",
            "exang": "Exercise Induced Angina",
            "oldpeak": "Oldpeak",
            "slope": "Slope",
            "ca": "No. of major vessels colored by flourosopy",
            "thal": "Thalassemia",
            "target": "",
        }

        widgets = {
            "target": forms.TextInput(attrs={"hidden": "", "value": "Unpredicted"}),
        }

    def clean_target(self):
        target = self.cleaned_data["target"]
        symptoms = {}

        #########################################

        if self.cleaned_data["sex"] == "Female":
            sex = 0
        elif self.cleaned_data["sex"] == "Male":
            sex = 1

        #########################################

        if self.cleaned_data["cp"] == "Typical angina":
            cp = 0
        elif self.cleaned_data["cp"] == "Atypical angina":
            cp = 1
        elif self.cleaned_data["cp"] == "Non-anginal pain":
            cp = 2
        elif self.cleaned_data["cp"] == "Asymptomatic":
            cp = 3

        #########################################

        if self.cleaned_data["fbs"] == "Lower than 120 mg/ml":
            fbs = 0
        elif self.cleaned_data["fbs"] == "Greater than 120 mg/ml":
            fbs = 1

        #########################################

        if self.cleaned_data["restecg"] == "Normal":
            restecg = 0
        elif self.cleaned_data["restecg"] == "ST-T wave abnormality":
            restecg = 1
        elif self.cleaned_data["restecg"] == "Left ventricular hypertrophy":
            restecg = 2

        #########################################

        if self.cleaned_data["exang"] == "No":
            exang = 0
        elif self.cleaned_data["exang"] == "Yes":
            exang = 1

        #########################################

        if self.cleaned_data["slope"] == "Upsloping":
            slope = 0
        elif self.cleaned_data["slope"] == "Flat":
            slope = 1
        elif self.cleaned_data["slope"] == "Downsloping":
            slope = 2

        #########################################

        if self.cleaned_data["ca"] == "Zero":
            ca = 0
        elif self.cleaned_data["ca"] == "One":
            ca = 1
        elif self.cleaned_data["ca"] == "Two":
            ca = 2
        elif self.cleaned_data["ca"] == "Three":
            ca = 3

        #########################################

        if self.cleaned_data["thal"] == "Normal":
            thal = 3
        elif self.cleaned_data["thal"] == "Fixed Defect":
            thal = 6
        elif self.cleaned_data["thal"] == "Reversable Defect":
            thal = 7

        #########################################

        symptoms["age"] = int(self.cleaned_data["age"])
        symptoms["sex"] = int(sex)
        symptoms["cp"] = int(cp)
        symptoms["trestbps"] = int(self.cleaned_data["trestbps"])
        symptoms["chol"] = int(self.cleaned_data["chol"])
        symptoms["fbs"] = int(fbs)
        symptoms["restecg"] = int(restecg)
        symptoms["thalach"] = int(self.cleaned_data["thalach"])
        symptoms["exang"] = int(exang)
        symptoms["oldpeak"] = float(self.cleaned_data["oldpeak"])
        symptoms["slope"] = int(slope)
        symptoms["ca"] = int(ca)
        symptoms["thal"] = int(thal)

        classifier = pickle.load(
            open("static\model\heart_attk_pred.pkl", "rb"))
        int_features = list(symptoms.values())
        final_features = [numpy.array(int_features)]
        output = classifier.predict(final_features)
        prediction = round(output[0], 2)

        if prediction == 0:
            target = "No Heart Disease"
        elif prediction == 1:
            target = "Heart Disease"

        return target
