from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from luck import isLucky


@csrf_exempt
def Luck(Response, luck_str):
    return HttpResponse(isLucky(str(luck_str)))
