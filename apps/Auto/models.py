from django.db import models

class Car(models.Model):
    Typ = models.CharField(max_length=100, null=True)
    Farbe = models.CharField(max_length=100, null=True)
    Hubraum = models.CharField(max_length=100, null=True)
    Zustand = models.CharField(max_length=100, null=True)
    Neupreis = models.CharField(max_length=100, null=True)
    Referenz = models.CharField(max_length=100, null=True)
    Zeitwert = models.CharField(max_length=100, null=True)
    Bereifung = models.CharField(max_length=100, null=True)
    Letzte_MFK = models.CharField(max_length=100, null=True)
    Ausstattung = models.TextField(null=True)
    Schaden_Nr = models.CharField(max_length=100, null=True)
    Typenschein = models.CharField(max_length=100, null=True)
    Reparaturkosten = models.CharField(max_length=100, null=True)
    Bauart_Aufbau_Türen = models.CharField(max_length=100, null=True)
