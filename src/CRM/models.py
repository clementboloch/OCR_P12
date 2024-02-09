from django.db import models
from django.conf import settings


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    commercial_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=50, null=True, blank=True)
    outstanding_amount = models.FloatField(max_length=50, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    is_signed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.outstanding_amount == None:
            self.outstanding_amount = self.amount
        super(Contract, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.client} - {self.created_date}"


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    attendees = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=10000, null=True, blank=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.contract.client} ({self.start_date} - {self.end_date})"
