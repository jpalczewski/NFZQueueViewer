# @file web/urls.py
#  @brief Django urls

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from providers.views import RecordListView, UpdateDatabase, GetDepartments, FlushDatabase
from providers.views_rest import ProviderViewSet, ProviderSectionViewSet, ProvisionViewSet, RecordViewSet


router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet, base_name='provider')
router.register(r'providersection', ProviderSectionViewSet, base_name='providersection')
router.register(r'provision', ProvisionViewSet,base_name='provision')
router.register(r'record', RecordViewSet,base_name='record')


urlpatterns = patterns( '',
                        url(r'^$', RecordListView.as_view(), name='index'),
                        url(r'^api/update/$', UpdateDatabase, name='update'),
                        url(r'^api/flush/$', FlushDatabase, name='Flush'),
                        url(r'^select/$', GetDepartments, name='select'),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^api/', include(router.urls))
            )
