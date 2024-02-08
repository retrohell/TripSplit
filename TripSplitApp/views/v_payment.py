import json
from django.http import JsonResponse
from django.db import IntegrityError
from ..models import Payment, Guest
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def createPayment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            payment = Payment.objects.create(
                payer_id = Guest.objects.get(id=data['payer_id']), # This is a foreign key from the Guest model
                receiver_id = Guest.objects.get(id=data['receiver_id']), # This is a foreign key from the Guest model
                amount = data['amount'],
            )
            payment.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating payment'}, status=400)
        
def getPayment(request, id):
    if request.method == 'GET':
        payment = Payment.objects.get(id=id)
        payment = serializers.serialize('json', [payment,])
        json_data = json.loads(payment)
        return JsonResponse(json_data, status=200, safe=False)