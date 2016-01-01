from models import Record, Provider, Provision, ProviderSection
from rest_framework import serializers


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('Name', 'NFZDepartment')


class ProviderSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProviderSection
        fields = ('RelatedProvider', 'Name', 'Address', 'City', 'Phone')


class ProvisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provision
        fields = (  'Name', 'UrgentApplicable',
                    'Urgent', 'AverageWaitingDays',
                    'WaitingCustomers', 'ServedCustomers',
                    'FirstAvailableDate'
        )


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('Pr', 'PS', 'Pn')
