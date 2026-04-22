# This script seeds the database with sample student data for testing and development.

import os, sys, django

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_analytics.settings') 
django.setup()

from app.models import Student

SAMPLE = [
    ("Aarav Sharma",   "R001",  88, 92),
    ("Priya Verma",    "R002",  75, 85),
    ("Rohit Gupta",    "R003",  62, 70),
    ("Sneha Patel",    "R004",  91, 96),
    ("Arjun Nair",     "R005",  45, 55),
    ("Kavya Iyer",     "R006",  33, 40),
    ("Vikram Singh",   "R007",  58, 68),
    ("Pooja Mehta",    "R008",  77, 82),
    ("Aditya Joshi",   "R009",  22, 25),
    ("Nisha Reddy",    "R010",  95, 98),
    ("Rahul Kumar",    "R011",  48, 52),
    ("Divya Mishra",   "R012",  67, 73),
]

created = 0
for name, roll, marks, att in SAMPLE:
    obj, new = Student.objects.get_or_create(
        roll_no=roll,
        defaults={"name": name, "marks": marks, "attendance": att}
    )
    if new:
        created += 1

print(f"✅  Seeded {created} students ({len(SAMPLE)-created} already existed).")