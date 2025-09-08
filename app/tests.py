from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import OpettajaViewSet, KurssiViewSet
from .models import Opettaja, Kurssi

class ViewSetTest(TestCase):
    def test_opettaja_viewset(self):
        '''Opettajan lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")
        ope_set = OpettajaViewSet.as_view({'get': 'retrieve'})
        ope = Opettaja.objects.create(nimi="Lena", puhelin="123456789")
        # pk tarkoittaa pääavainta eli id:tä /api/opettajat/1/
        response = ope_set(request, pk=ope.pk)
        # testataan että saatiin 200 OK vastaus
        self.assertEqual(response.status_code, 200)
        # testataan että objekti liotiin juuri sellaiseksi kuin piti
        self.assertEqual(response.data, {'id': 1, 'nimi': 'Lena', 'puhelin': '123456789'})

    def test_kurssi_viewset(self):
        '''Kurssin lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")

        # Kurssiin lisääminen tarvitsee ensin luoda opettaja
        ope_set = OpettajaViewSet.as_view({'get': 'retrieve'})
        ope = Opettaja.objects.create(nimi="Lena", puhelin="123456789")

        kur_set = KurssiViewSet.as_view({'get': 'retrieve'})
        kurssi = Kurssi.objects.create(nimi="Django", laajuus=5, opettaja_id=ope.pk)

        response = kur_set(request, pk=kurssi.pk)

        # testataan että saatiin 200 OK vastaus
        self.assertEqual(response.status_code, 200)
        # testataan että objekti liotiin juuri sellaiseksi kuin piti
        self.assertEqual(response.data, {'id': 1, 'nimi': 'Django', 'laajuus': 5, 'opettaja': 1, 'opettaja_id': 1})