from luck import isLucky
from django.http import HttpResponse


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def Luck(Response, luck_str):
    return HttpResponse(isLucky(str(luck_str)))
