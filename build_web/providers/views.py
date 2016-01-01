from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Provider, ProviderSection, Provision, Record
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from .forms import UpdateForm
from django.utils import timezone
from django.db import IntegrityError
import re
import os
import glob
import datetime
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


def UpdateDatabase(request):
    SelectedNFZDepartments = request.POST.getlist('departments')
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


def GenerateRecords():
    for provider in Provider.objects.all():
        for ps in provider.providersection_set.all():
            for  prov in ps.provision_set.all():
                d = Record(Pr=provider, PS=ps, Pn=prov)
                d.save()


def profile(log_file):
    """Profile some callable.

    This decorator uses the hotshot profiler to profile some callable (like
    a view function or method) and dumps the profile data somewhere sensible
    for later processing and examination.

    It takes one argument, the profile log name. If it's a relative path, it
    places it under the PROFILE_LOG_BASE. It also inserts a time stamp into the
    file name, such that 'my_view.prof' become 'my_view-20100211T170321.prof',
    where the time stamp is in UTC. This makes it easy to run and compare
    multiple trials.
    """

    if not os.path.isabs(log_file):
        log_file = os.path.join(PROFILE_LOG_BASE, log_file)

    def _outer(f):
        def _inner(*args, **kwargs):
            # Add a timestamp to the profile output when the callable
            # is actually called.
            (base, ext) = os.path.splitext(log_file)
            base = base + "-" + time.strftime("%Y%m%dT%H%M%S", time.gmtime())
            final_log_file = base + ext

            prof = hotshot.Profile(final_log_file)
            try:
                ret = prof.runcall(f, *args, **kwargs)
            finally:
                prof.close()
            return ret

        return _inner
    return _outer

try:
    PROFILE_LOG_BASE = settings.PROFILE_LOG_BASE
except:
    PROFILE_LOG_BASE = tempfile.gettempdir()


@profile("readxlsxfile")
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

        a, cr = Provider.objects.get_or_create(Name=row[2].value, NFZDepartment=depno)
        b, cr = ProviderSection.objects.get_or_create(RelatedProvider=a, Name=row[3].value, Address=address, City=city, Phone=phone)
        c, cr = Provision.objects.get_or_create(Name=row[0].value, UrgentApplicable=ua, Urgent=u, AverageWaitingDays=int_noexcept(row[7].value), ServedCustomers=int_noexcept(row[6].value), WaitingCustomers=int_noexcept(row[5].value), FirstAvailableDate=parse_date(row[9].value), RelatedProviderSection=b)
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
    if type(s)==str:
        return '1970-01-01'
    else:
        return s
