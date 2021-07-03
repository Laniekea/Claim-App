from claims.settings import MEDIA_ROOT
from django.db import models
from django.conf import settings
from django.contrib import auth 

class Vehicle(models.Model):
    id = models.AutoField(primary_key="true")
    vehicle_model = models.CharField(max_length=200)
    vehicle_number = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicle_model

class Loss(models.Model):
    STATUS = (
        (1, ('Own Damage')),
        (2, ('Knock of Knock')),
        (3, ('Windscreen Damage')),
        (4, ('Theft'))
    )

    id = models.AutoField(primary_key="true")
    datetime = models.DateTimeField('datetime of accident')
    location = models.CharField(max_length=254)
    loss_type = models.IntegerField(choices=STATUS)
    description = models.TextField()
    police_report_lodge = models.BooleanField()
    injured_status = models.BooleanField()

class Document(models.Model):
    id = models.AutoField(primary_key="true")
    photo = models.ImageField(upload_to=MEDIA_ROOT)
    pdf = models.FileField(upload_to='pdf')

class Claim(models.Model):
    STATUS = (
        ('in progress', ('In Progress')),
        ('accepted', ('Accepted'))
    )
    id = models.AutoField(primary_key="true")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    loss_id = models.ForeignKey(Loss, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS)