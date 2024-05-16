from django.db import models

class ContactRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('info', 'Demande d\'info'),
        ('other', 'Autre demande'),
    ]

    type_of_request = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    observations = models.TextField()

    def __str__(self):
        return self.full_name
