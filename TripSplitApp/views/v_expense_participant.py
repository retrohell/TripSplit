from ..models import ExpenseParticipant
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_expense_participant import ReadExpenseParticipantSerializer, WriteExpenseParticipantSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, permissions
from rest_framework_simplejwt import authentication

class ExpenseParticipantView(APIView):
    authentication_classes = [authentication.JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    
    def post(self, request):
        data = request.data
        expenseserializer = WriteExpenseParticipantSerializer(data=data)
        try:
            if expenseserializer.is_valid(raise_exception=True):
                expenseserializer.save()
                return JsonResponse(expenseserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)
        
    def get(self, request, id):
        try:
            expense = ExpenseParticipant.objects.get(id=id)
            dataserilizer = ReadExpenseParticipantSerializer(expense).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Expense does not exist'}, status=404)
        
    def put(self, request, id):
        try:
            data = request.data
            expense = ExpenseParticipant.objects.get(id=id)
            expenseserializer = WriteExpenseParticipantSerializer(expense, data=data, partial=True)
            if expenseserializer.is_valid(raise_exception=True):
                expenseserializer.save()
                return JsonResponse(expenseserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def delete(self, request, id):
        try:
            expense = ExpenseParticipant.objects.get(id=id)
            expense.delete()
            return JsonResponse({'message': 'Expense participant deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Expense participant does not exist'}, status=404)



# import json
# from django.http import JsonResponse
# from django.db import IntegrityError
# from ..models import ExpenseParticipant, Guest, Expense
# from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers

# @csrf_exempt
# def createExpenseParticipant(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         try:
#             expenseParticipant = ExpenseParticipant.objects.create(
#                 expense_id = Expense.objects.get(id=data['expense_id']), # This is a foreign key from the Expense model
#                 participant_id = Guest.objects.get(id=data['guest_id']), # This is a foreign key from the Guest model
#             )
#             expenseParticipant.save()
#             return JsonResponse(data, status=200)
#         except IntegrityError as e:
#             print(e)
#             return JsonResponse({'error': 'Error creating expense participant'}, status=400)
        
# def getExpenseParticipant(request, id):
#     if request.method == 'GET':
#         expenseParticipant = ExpenseParticipant.objects.get(id=id)
#         expenseParticipant = serializers.serialize('json', [expenseParticipant,])
#         json_data = json.loads(expenseParticipant)
#         return JsonResponse(json_data, status=200, safe=False)