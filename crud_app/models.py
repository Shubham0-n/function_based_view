from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    profile_image = models.ImageField(upload_to="images", null=True)
    first_name = models.CharField(max_length=250, db_index=True)
    last_name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(max_length=250, unique=True)
    birthdate = models.DateField(help_text="Add Birthdate")
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
