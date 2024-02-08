import json
from ..models import Guest
from rest_framework.views import APIView
from django.http import JsonResponse


class GuestView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        guest = Guest.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            user_id=data['user_id']
        )
        return JsonResponse({'guest': guest.id}, status=201)

    def get(self, request, id):
        guest = Guest.objects.get(id=id)
        return JsonResponse({
            'id': str(guest.id),
            'username': guest.username,
            'email': guest.email,
            'password': guest.password,
            'user_id': guest.id
        })
    
    def put(self, request, id):
        data = json.loads(request.body)
        guest = Guest.objects.get(id=id)
        if 'username' in data:
            guest.username = data['username']
        if 'email' in data:
            guest.email = data['email']
        if 'password' in data:
            guest.password = data['password']
        guest.save()
        return JsonResponse({'message': 'Guest updated successfully'}, status=200)
    
    def delete(self, request, id):
        guest = Guest.objects.get(id=id)
        guest.delete()
        return JsonResponse({'message': 'Guest deleted successfully'}, status=200)