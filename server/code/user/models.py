from django.db import models

class User(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    DOB = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.id
