# Generated by Django 5.1.7 on 2025-03-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0003_alter_cart_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file_path",
            field=models.FileField(upload_to="images/"),
        ),
    ]
