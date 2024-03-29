from ..models import Expense, Guest
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_expense import ReadExpenseSerializer, WriteExpenseSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, permissions
import rest_framework_simplejwt


class ExpenseView(APIView):
    # Autenticacion y permisos
    authentication_classes = [
        rest_framework_simplejwt.authentication.JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        data = request.data
        # Se obtiene el id del usuario que esta realizando la peticion
        try:
            guest = Guest.objects.get(user_id=request.user.id)
            data['payer'] = guest.id
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Guest does not exist'}, status=404)
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
            expenseserializer = WriteExpenseSerializer(
                expense, data=data, partial=True)
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


class ExpenseViewList(APIView):
    authentication_classes = [
        rest_framework_simplejwt.authentication.JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        try:
            guest = Guest.objects.get(user_id=request.user.id)
            expenses = Expense.objects.filter(payer=guest)
            expenseSerializer = ReadExpenseSerializer(expenses, many=True)
            return JsonResponse(expenseSerializer.data, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'There are no expenses'}, status=404)
