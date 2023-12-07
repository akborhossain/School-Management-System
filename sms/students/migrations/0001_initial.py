# Generated by Django 5.0 on 2023-12-07 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
            fields=[
                (
                    "student_id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("username", models.CharField(default="", max_length=10, unique=True)),
                (
                    "password",
                    models.CharField(
                        default="pbkdf2_sha256$720000$sRMKrD7mqNWYp4IiJYhV5U$6FTRD7s3rBj6bKnS2KNAEXLXlpyBMY7cN8IfnLgGLX0=",
                        max_length=128,
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("birth_number", models.CharField(max_length=17, unique=True)),
                ("father_name", models.CharField(max_length=150)),
                ("father_nid", models.IntegerField()),
                ("mother_name", models.CharField(max_length=150)),
                ("mother_nid", models.IntegerField()),
                ("phone_number", models.CharField(max_length=11)),
                ("present_address", models.CharField(max_length=500)),
                ("parmanent_address", models.CharField(max_length=500)),
                ("image", models.CharField(default="", max_length=25)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "class_id",
                    models.CharField(
                        choices=[
                            (" ", "Select Class"),
                            ("Pre-One", "Pre-One"),
                            ("One", "One"),
                            ("Two", "Two"),
                            ("Three", "Three"),
                            ("Four", "Four"),
                            ("Five", "Five"),
                            ("Six", "Six"),
                            ("Seven", "Seven"),
                            ("Eight", "Eight"),
                            ("Nine", "Nine"),
                            ("Ten", "Ten"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "group",
                    models.CharField(
                        choices=[
                            ("", "Select Department"),
                            ("General", "General"),
                            ("Science", "Science"),
                            ("Commerce", "Commerce"),
                            ("Humanity", "Humanity"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
            ],
        ),
    ]
