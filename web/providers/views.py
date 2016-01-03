from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from .models import Provider, ProviderSection, Provision, Record
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from .forms import UpdateForm
from django.utils import timezone
from django.db import IntegrityError
import re
import os
import glob
import datetime
import json
from config.settings import BASE_DIR
from openpyxl import load_workbook
import hotshot
import os
import time
import config.settings
import tempfile

class RecordListView(ListView):
    model = Record
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def GetDepartments(request):
    form = UpdateForm()
    return render(request, 'update.html', {'form': form})


def FlushDatabase(request):
    Provider.objects.all().delete()
    return HttpResponse("ok")


@csrf_exempt
def UpdateDatabase(request):
    SelectedNFZDepartments = json.loads(request.body)['departments']
    #checker = re.compile("\d+")
    #for param in SelectedNFZDepartments:
    #    if checker.search(param) != None:
    #        return HttpResponseBadRequest("You are a bad boy, aren't you?")

    root_dir = os.path.dirname(BASE_DIR)
    files_dir = os.path.join(os.path.join(root_dir, 'NFZSpider'), 'files')

    our_files = glob.glob(os.path.join(files_dir, '*'))
    out_files = []
    for param in SelectedNFZDepartments:
        out_files.append(filter(lambda x: param + '_' in x, our_files))

    for f in out_files:
        readxlsxfile(f[0])

    return HttpResponse("ok")


def readxlsxfile(file):
    depno = int(os.path.basename(file)[0:2])

    wb = load_workbook(file, read_only=True)
    ws = wb.active

    skipme = 3
    for row in ws.rows:
        if skipme:
            skipme = skipme - 1
            continue

        city, address, phone = row[4].value.split('\n')
        ua, u = parse_urgent(row[1].value)

        date = row[9].value
        parsed_date = parse_date(date)

        a, cr = Provider.objects.get_or_create(Name=row[2].value, NFZDepartment=depno)
        b, cr = ProviderSection.objects.get_or_create(RelatedProvider=a, Name=row[3].value, Address=address, City=city, Phone=phone)
        c, cr = Provision.objects.get_or_create(Name=row[0].value, UrgentApplicable=ua, Urgent=u, AverageWaitingDays=int_noexcept(row[7].value), ServedCustomers=int_noexcept(row[6].value), WaitingCustomers=int_noexcept(row[5].value), FirstAvailableDate=parsed_date, RelatedProviderSection=b)
        d  = Record(Pr=a, PS=b, Pn=c)
        try:
            a.save()
            b.save()
            c.save()
            d.save()
        except IntegrityError:
            continue


def int_noexcept(s):
    try:
        return int(s)
    except ValueError:
        return 0


def parse_urgent(s):
    if s == '-':
        return False, False
    else:
        if(s=='Przypadek stabilny'):
            return True,False
        else:
            return True,True

def parse_date(s):
    if type(s) is unicode:
        return '1970-01-01'
    else:
        return s
