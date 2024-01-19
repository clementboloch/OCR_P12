from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    commercial_contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=50)
    outstading_amount = models.FloatField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    is_signed = models.BooleanField(default=False)


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)
    attendees = models.IntegerField()
    notes = models.TextField(max_length=10000)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
