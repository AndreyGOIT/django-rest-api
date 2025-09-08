from django.db import models

# Create your models here.
class Opettaja(models.Model):
    nimi = models.CharField(max_length=100, default="")
    puhelin = models.CharField(max_length=20, default="")

    class Meta:
        ordering = ['nimi']
    
class Kurssi(models.Model):
    nimi = models.CharField(max_length=100, default="")
    laajuus = models.IntegerField(default=0)  # laajuus opintopisteinä
    opettaja = models.ForeignKey(Opettaja, on_delete=models.CASCADE, related_name='kurssit')

    class Meta:
        ordering = ['nimi']
