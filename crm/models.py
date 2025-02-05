from django.db import models


class Membership(models.Model):

    name = models.CharField(max_length=500)

    MEMBERSHIP_CHOICES = (
        ("s", "Standard"),
        ("p", "Premium"),
        ("ux", "Ultimate Delux"),
    )

    membership_plan = models.CharField(max_length=2, choices=MEMBERSHIP_CHOICES)
    membership_active =models.BooleanField(default=True)
    unique_code = models.CharField(max_length=250)