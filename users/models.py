from django.db import models
from django.contrib.auth.models import User

Junior_club = 'Junior'
Middle_club = 'Middle'
Senior_club = 'Senior'

class CustomUser(User):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, default='+996000000000')
    whats_phone = models.CharField(max_length=14, default='+996000000000')
    experience = models.PositiveIntegerField(default=2)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    club = models.CharField(max_length=100,null=True, blank=True)

    def save(self, *args, **kwargs):
        if 0 < self.experience <= 3:
            self.club = Junior_club
        elif 3 < self.experience <= 6:
            self.club = Middle_club
        elif 6 < self.experience <= 50:
            self.club = Senior_club
        else:
            self.club = None
        super().save(*args, **kwargs)


