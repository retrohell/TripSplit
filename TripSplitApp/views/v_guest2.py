# import json
from ..models import Guest
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_guest import ReadGuestSerializer, WriteGuestSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from ..serializers.s_user import WriteUserSerializer, ReadUserSerializer
from django.db import transaction # Para operaciones atomicas

class GuestView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    authentication_classes = [authentication.JWTAuthentication,]

    def post(self, request):
        data = request.data

        # Validar operacion atomica de la creacion de usuario y guest
        try:
            with transaction.atomic(): # Para operaciones atomicas
                newUserSerializer = WriteUserSerializer(data=data)
                if newUserSerializer.is_valid(raise_exception=True):
                    newUserSerializer.save()
                    data['user'] = newUserSerializer.data['id']
                guestserializer = WriteGuestSerializer(data=data)
                if guestserializer.is_valid(raise_exception=True):
                    guestserializer.save()
                    return JsonResponse(guestserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

        # data = json.loads(request.body)
        # guest = Guest.objects.create(
        #     username=data['username'],
        #     email=data['email'],
        #     password=data['password'],
        #     user_id=data['user_id']
        # )
        # return JsonResponse({'guest': guest.id}, status=201)

    def get(self, request):
        try:
            print(request.user.username)
            guest = Guest.objects.get(user=request.user.id)
            dataserilizer = ReadGuestSerializer(guest).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Guest does not exist'}, status=404)

    def put(self, request, id):
        try:
            data = request.data
            guest = Guest.objects.get(id=id)
            guestserializer = WriteGuestSerializer(
                guest, data=data, partial=True)
            if guestserializer.is_valid(raise_exception=True):
                guestserializer.save()
                return JsonResponse(guestserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

        # data = json.loads(request.body)
        # guest = Guest.objects.get(id=id)
        # if 'username' in data:
        #     guest.username = data['username']
        # if 'email' in data:
        #     guest.email = data['email']
        # if 'password' in data:
        #     guest.password = data['password']
        # guest.save()
        # return JsonResponse({'message': 'Guest updated successfully'}, status=200)

    def delete(self, request, id):
        guest = Guest.objects.get(id=id)
        guest.delete()
        return JsonResponse({'message': 'Guest deleted successfully'}, status=200)

