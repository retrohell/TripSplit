import json
from django.http import JsonResponse
from django.db import IntegrityError
from django.core import serializers
from ..models import Expense, Guest
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import localdate

# 23e63dbd-05cd-41a1-8e1d-b492cc7f95c8

@csrf_exempt
def createExpense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            expense = Expense.objects.create(
                payer = Guest.objects.get(id=data['guest_id']), # This is a foreign key from the Guest model
                amount = data['amount'],
                description = data['description'],
                updated_at = localdate()
            )
            expense.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating expense'}, status=400)
        
def getExpense(request, id):
    if request.method == 'GET':
        expense = Expense.objects.get(id=id)
        expense = serializers.serialize('json', [expense,])
        json_data = json.loads(expense)
        return JsonResponse(json_data, status=200, safe=False)