from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'opettajat', views.OpettajaViewSet, 'opettaja-nimi')
router.register(r'kurssit', views.KurssiViewSet, 'kurssi-nimi')


urlpatterns = [
    path('api/', include((router.urls, "app"))),
]