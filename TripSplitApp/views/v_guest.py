import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Guest
from django.db import IntegrityError
from django.core import serializers

# Payment, Group, Expense
# Create POST


@csrf_exempt
def createGuest(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['nombre'])
        try:
            guest = Guest.objects.create(
                username=data['nombre'],
                email=data['email'],
                password=data['password'],
                user_id=data['user_id']
            )
            guest.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating guest'}, status=400)


def getGuest(request, id):
    if request.method == 'GET':
        guest = Guest.objects.get(id=id)
        guest = serializers.serialize('json', [guest,])
        json_data = json.loads(guest)
        return JsonResponse(json_data, status=200, safe=False)
