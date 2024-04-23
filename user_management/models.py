#user_management/models.py

from django.db import models

class User(models.Model):
    employee_id = models.CharField(max_length=50, primary_key=True)
    employee_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)

    def __str__(self):
        return self.employee_id
