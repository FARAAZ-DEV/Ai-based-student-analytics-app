from django.db import models

class Student(models.Model): # Student class inherits models.Model
# This inheritance registers Student with the database defined in settings.py
    name       = models.CharField(max_length=100) 
    roll_no    = models.CharField(max_length=20, unique=True)
    marks      = models.FloatField()          # 0–100
    attendance = models.FloatField()          # 0–100 (%)

    def __str__(self):
        return f"{self.roll_no} – {self.name}"
