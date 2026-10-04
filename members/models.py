from django.db import models


class Member(models.Model):

    PROGRAM_CHOICES = [
        ("Strength Training", "Strength Training"),
        ("Cardio Training", "Cardio Training"),
        ("Fat Loss", "Fat Loss"),
        ("Functional Training", "Functional Training"),
        ("Yoga & Flexibility", "Yoga & Flexibility"),
        ("HIIT Workout", "HIIT Workout"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

    program = models.CharField(max_length=50, choices=PROGRAM_CHOICES)

    def __str__(self):
        return self.name
