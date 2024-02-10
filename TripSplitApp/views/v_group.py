from ..models import Group
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_group import ReadGroupSerializer, WriteGroupSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, permissions
from rest_framework_simplejwt import authentication

class GroupView(APIView):
    authentication_classes = [authentication.JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    
    def post(self, request):
        data = request.data
        groupserializer = WriteGroupSerializer(data=data)
        try:
            if groupserializer.is_valid(raise_exception=True):
                groupserializer.save()
                return JsonResponse(groupserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)
        
    def get(self, request, id):
        try:
            group = Group.objects.get(id=id)
            dataserilizer = ReadGroupSerializer(group).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Group does not exist'}, status=404)
        
    def put(self, request, id):
        try:
            data = request.data
            group = Group.objects.get(id=id)
            groupserializer = WriteGroupSerializer(group, data=data, partial=True)
            if groupserializer.is_valid(raise_exception=True):
                groupserializer.save()
                return JsonResponse(groupserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def delete(self, request, id):
        try:
            group = Group.objects.get(id=id)
            group.delete()
            return JsonResponse({'message': 'Group deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Group does not exist'}, status=404)