from django.db import models
from django.db.models import DateTimeField


# Create your models here.

class Party(models.Model):
    name_party = models.CharField(max_length=50, blank=True)
    image_party = models.ImageField(upload_to='media/databaseImageParty', blank=True)
    info_party = models.TextField(blank=True)
    age_party = models.IntegerField(blank=True)


class LocalsParty(models.Model):
    address = models.CharField(max_length=50, blank=True)
    nameLocal = models.TextField(blank=True)
    map_party = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/databaseImageLocal', blank=True)


class Tickets(models.Model):
    price = models.IntegerField(blank=True)
    name_party = models.CharField(max_length=50, blank=True)
    date = DateTimeField(blank=True)
    count_ticket = models.IntegerField(blank=True)
    ID_Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    ID_Local = models.ForeignKey(LocalsParty, on_delete=models.CASCADE)



