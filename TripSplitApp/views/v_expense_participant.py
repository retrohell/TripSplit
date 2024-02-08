import json
from django.http import JsonResponse
from django.db import IntegrityError
from ..models import ExpenseParticipant, Guest, Expense
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def createExpenseParticipant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            expenseParticipant = ExpenseParticipant.objects.create(
                expense_id = Expense.objects.get(id=data['expense_id']), # This is a foreign key from the Expense model
                participant_id = Guest.objects.get(id=data['guest_id']), # This is a foreign key from the Guest model
            )
            expenseParticipant.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating expense participant'}, status=400)
        
def getExpenseParticipant(request, id):
    if request.method == 'GET':
        expenseParticipant = ExpenseParticipant.objects.get(id=id)
        expenseParticipant = serializers.serialize('json', [expenseParticipant,])
        json_data = json.loads(expenseParticipant)
        return JsonResponse(json_data, status=200, safe=False)