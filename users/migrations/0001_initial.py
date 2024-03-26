# Generated by Django 5.0.3 on 2024-03-26 21:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('relationship', models.CharField(choices=[('SON', 'Son'), ('DAUGHTER', 'Daughter'), ('SPOUSE', 'Spouse'), ('OTHER', 'Other')], max_length=50, verbose_name='Relationship')),
                ('other_relationship', models.CharField(blank=True, max_length=100, null=True, verbose_name='Other Relationship')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dependent',
                'verbose_name_plural': 'Dependents',
            },
        ),
    ]
