from django.db import models
from django.contrib.auth.models import User

class Dependente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    relationship_choices = [
        ('SON', 'Son'),
        ('DAUGHTER', 'Daughter'),
        ('SPOUSE', 'Spouse'),
        ('OTHER', 'Other'),
    ]
    relationship = models.CharField(max_length=50, choices=relationship_choices, verbose_name='Relationship')

    class Meta:
        verbose_name = 'Dependent'
        verbose_name_plural = 'Dependents'

    def __str__(self):
        return self.name
