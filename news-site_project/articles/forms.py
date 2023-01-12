from django import forms
from .models import Articles
from sklearn.feature_extraction.text import CountVectorizer
import datetime
import pandas as pd
import pickle


class ArticlesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.content = kwargs.pop("content", None)
        super(ArticlesForm, self).__init__(*args, **kwargs)

    category = forms.ChoiceField(
        label="Pick Category",
        choices=[
            ("Uncategorized", ""),
            ("Business News", "Business News"),
            ("Tech News", "Tech News"),
            ("Politics News", "Politics News"),
            ("Sports News", "Sports News"),
            ("Entertainment News", "Entertainment News"),
        ],
    )

    class Meta:
        model = Articles
        fields = (
            "pub_date",
            "category",
            "content",
            "reporter",
        )
        labels = {
            "content": "Write your article here",
            "pub_date": "",
            "reporter": "",
        }

        widgets = {
            "pub_date": forms.DateInput(attrs={"hidden": "", "value": datetime.date.today()}),
            "reporter": forms.NumberInput(attrs={"hidden": "", "value": 1}),
            "category": forms.TextInput(attrs={"value": "Uncategorized"}),
        }

    def clean_category(self):

        category = self.cleaned_data["category"]

        if category == "Uncategorized":

            bag_of_words = pd.read_json("static/temp/vocabulary.json")
            cv = CountVectorizer(max_features=5000)
            cv.fit_transform(bag_of_words.Text).toarray()
            classifier = pickle.load(
                open("static/model/classifier_text.pkl", "rb"))
            y_pred1 = cv.transform([self.content])
            yy = classifier.predict(y_pred1)
            if yy == [0]:
                result = "Business News"
            elif yy == [1]:
                result = "Tech News"
            elif yy == [2]:
                result = "Politics News"
            elif yy == [3]:
                result = "Sports News"
            elif yy == [4]:
                result = "Entertainment News"

            category = result

            return category
        else:
            return category

    def clean_reporter(self):
        reporter = self.cleaned_data["reporter"]
        reporter = self.user

        return reporter


class DocumentForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


def handle_uploaded_file(f,user):

    with open('media/uploads/temp.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    try:
        text = []
        with open('media/uploads/temp.txt') as f:
            text = f.readlines()
        bag_of_words = pd.read_json("static/temp/vocabulary.json")
        cv = CountVectorizer(max_features=5000)
        cv.fit_transform(bag_of_words.Text).toarray()
        classifier = pickle.load(
            open("static/model/classifier_text.pkl", "rb"))
        y_pred1 = cv.transform(text)
        yy = classifier.predict(y_pred1)
        result = ""
        if yy == [0]:
            result = "Business News"
        elif yy == [1]:
            result = "Tech News"
        elif yy == [2]:
            result = "Politics News"
        elif yy == [3]:
            result = "Sports News"
        elif yy == [4]:
            result = "Entertainment News"

        Articles.objects.create(pub_date=datetime.date.today(), category=result, content=text[0],reporter=user)
        return "Article has been published"

    except:
        return "Error! Failed to publish article"
