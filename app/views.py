from rest_framework import viewsets
from .models import Opettaja, Kurssi
from .serializers import OpettajaSerializer, KurssiSerializer

''' A.o metodi osaa tehdä kaikki CRUD operaatiot
    GET, POST, PUT, DELETE ja hakea opettajat:
    -kaikki opettajat: /api/opettajat/
    -opettajan id:llä /api/opettajat/1/
    -opettajat nimen perusteella: /api/opettajat/?nimi=joku_nimi
'''

class OpettajaViewSet(viewsets.ModelViewSet):
    serializer_class = OpettajaSerializer

    def get_queryset(self):
        queryset = Opettaja.objects.all()
        nimi = self.request.query_params.get('nimi')
        if nimi is not None:
            queryset = queryset.filter(nimi=nimi)
        return queryset

''' A.o metodi osaa tehdä kaikki CRUD operaatiot 
    GET, POST, PUT, DELETE ja hakea kurssit:
    -kaikki kurssit: /api/kurssit/
    -kurssi id:llä /api/kurssit/1/
    -kurssit nimen perusteella: /api/kurssit/?nimi=joku_nimi
    -kurssit opettajan id:llä /api/kurssit/?opettaja=opettaja_id
'''
class KurssiViewSet(viewsets.ModelViewSet):
    serializer_class = KurssiSerializer

    def get_queryset(self):
        queryset = Kurssi.objects.all()
        nimi = self.request.query_params.get('nimi')
        opettaja = self.request.query_params.get('opettaja')
        if nimi is not None:
            queryset = queryset.filter(nimi=nimi)
        if opettaja is not None:
            queryset = queryset.filter(opettaja=opettaja)
        return queryset