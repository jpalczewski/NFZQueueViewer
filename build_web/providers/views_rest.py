from models import Record, Provider, Provision, ProviderSection
from rest_framework import viewsets
from serializers import ProviderSerializer, ProviderSectionSerializer, ProvisionSerializer, RecordSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('Name')
    serializer_class = ProviderSerializer


class ProviderSectionViewSet(viewsets.ModelViewSet):
    queryset = ProviderSection.objects.all().order_by('Name')
    serializer_class = ProviderSectionSerializer


class ProvisionViewSet(viewsets.ModelViewSet):
    queryset = Provision.objects.all().order_by('Name')
    serializer_class = ProvisionSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
