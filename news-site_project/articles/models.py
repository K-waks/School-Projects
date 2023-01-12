from django.db import models
from django.contrib.auth.models import User

# class Document(models.Model):
#     docfile = models.FileField(upload_to='uploads')

class Articles(models.Model):
    pub_date = models.DateField()
    category = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reporter"
    )

    def __str__(self):
        return self.content

