# Generated by Django 4.1.4 on 2022-12-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="articles",
            old_name="headline",
            new_name="category",
        ),
    ]