from ..models import Payment
from rest_framework.views import APIView
from ..serializers.s_payment import ReadPaymentSerializer, WritePaymentSerializer
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, permissions
from rest_framework_simplejwt import authentication


class PaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    authentication_classes = [authentication.JWTAuthentication,]

    def post(self, request):
        data = request.data
        paymentserializer = WritePaymentSerializer(data=data)
        try:
            if paymentserializer.is_valid(raise_exception=True):
                paymentserializer.save()
                return JsonResponse(paymentserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def get(self, request, id):
        try:
            payment = Payment.objects.get(id=id)
            dataserilizer = ReadPaymentSerializer(payment).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Payment does not exist'}, status=404)

    def put(self, request, id):
        try:
            data = request.data
            payment = Payment.objects.get(id=id)
            paymentserializer = WritePaymentSerializer(
                payment, data=data, partial=True)
            if paymentserializer.is_valid(raise_exception=True):
                paymentserializer.save()
                return JsonResponse(paymentserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def delete(self, request, id):
        try:
            payment = Payment.objects.get(id=id)
            payment.delete()
            return JsonResponse({'message': 'Payment deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Payment does not exist'}, status=404)
