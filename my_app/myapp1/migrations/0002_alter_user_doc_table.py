# Generated by Django 5.1.7 on 2025-03-18 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="user_doc",
            table="users_to_docs",
        ),
    ]
