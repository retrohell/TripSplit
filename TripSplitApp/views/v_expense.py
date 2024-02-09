from ..models import Expense
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_expense import ReadExpenseSerializer, WriteExpenseSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

class ExpenseView(APIView):
    def post(self, request):
        data = request.data
        expenseserializer = WriteExpenseSerializer(data=data)
        try:
            if expenseserializer.is_valid(raise_exception=True):
                expenseserializer.save()
                return JsonResponse(expenseserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)
        
    def get(self, request, id):
        try:
            expense = Expense.objects.get(id=id)
            dataserilizer = ReadExpenseSerializer(expense).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Expense does not exist'}, status=404)
        
    def put(self, request, id):
        try:
            data = request.data
            expense = Expense.objects.get(id=id)
            expenseserializer = WriteExpenseSerializer(expense, data=data, partial=True)
            if expenseserializer.is_valid(raise_exception=True):
                expenseserializer.save()
                return JsonResponse(expenseserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def delete(self, request, id):
        try:
            expense = Expense.objects.get(id=id)
            expense.delete()
            return JsonResponse({'message': 'Expense deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Expense does not exist'}, status=404)