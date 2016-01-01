from django.contrib import admin
from .models import Provider, Provision, ProviderSection,Record
# Register your models here.

admin.site.register(Provider)
admin.site.register(ProviderSection)
admin.site.register(Provision)
admin.site.register(Record)
