from django.db import models

# Create your models here.

class Provider(models.Model):
    Name = models.CharField(max_length=300)
    NFZDepartment = models.DecimalField(max_digits=2,decimal_places=0)
    def __unicode__(self):
        return self.Name

class ProviderSection(models.Model):
    RelatedProvider=models.ForeignKey(Provider)
    Name=models.CharField(max_length=300)
    Address=models.CharField(max_length=300)
    City=models.CharField(max_length=300)
    Phone=models.CharField(max_length=30)
    def __unicode__(self):
        return self.Name

class Provision(models.Model):
    RelatedProviderSection=models.ForeignKey(ProviderSection)

    Name=models.CharField(max_length=300)
    UrgentApplicable=models.BooleanField()
    Urgent=models.BooleanField()
    AverageWaitingDays=models.PositiveSmallIntegerField()
    WaitingCustomers=models.PositiveSmallIntegerField()
    ServedCustomers=models.PositiveSmallIntegerField()
    FirstAvailableDate=models.DateField()
    def __unicode__(self):
        return self.Name

class Record(models.Model):
    Pr = models.ForeignKey(Provider)
    PS = models.ForeignKey(ProviderSection)
    Pn = models.ForeignKey(Provision)

    def __unicode__(self):
        return self.Pr.Name + " - " + self.PS.Name + " - " + self.Pn.Name
