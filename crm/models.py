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

    def __str__(self):
        return self.name + " - record"
    
    class Meta:

        verbose_name_plural = "Membership"
        ordering = ["unique_code", "name"]