from django.db import models
from django.contrib.auth.models import User

class Dependent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    relationship_choices = [
        ('SON', 'Son'),
        ('DAUGHTER', 'Daughter'),
        ('SPOUSE', 'Spouse'),
        ('OTHER', 'Other'),
    ]
    relationship = models.CharField(max_length=50, choices=relationship_choices, verbose_name='Relationship')
    other_relationship = models.CharField(max_length=100, blank=True, null=True, verbose_name='Other Relationship')

    class Meta:
        verbose_name = 'Dependent'
        verbose_name_plural = 'Dependents'

    def __str__(self):
        return  f"{self.user.username}{self.name}"


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='profile_images', default='profile_images/default.png')

    def __str__(self):
        return self.user.username
