from ..models import UserGroup
from rest_framework.views import APIView
from django.http import JsonResponse
from ..serializers.s_user_group import ReadUserGroupSerializer, WriteUserGroupSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

class UserGroupView(APIView):
    def post(self, request):
        data = request.data
        usergroupserializer = WriteUserGroupSerializer(data=data)
        try:
            if usergroupserializer.is_valid(raise_exception=True):
                usergroupserializer.save()
                return JsonResponse(usergroupserializer.data, status=201)
        except ValidationError as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)
        
    def get(self, request, id):
        try:
            usergroup = UserGroup.objects.get(id=id)
            dataserilizer = ReadUserGroupSerializer(usergroup).data
            return JsonResponse(dataserilizer, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'User group does not exist'}, status=404)
        
    def put(self, request, id):
        try:
            data = request.data
            usergroup = UserGroup.objects.get(id=id)
            usergroupserializer = WriteUserGroupSerializer(usergroup, data=data, partial=True)
            if usergroupserializer.is_valid(raise_exception=True):
                usergroupserializer.save()
                return JsonResponse(usergroupserializer.data, status=200)
        except (ValidationError, ObjectDoesNotExist) as e:
            print(e)
            return JsonResponse({'message': 'Invalid data'}, status=400)

    def delete(self, request, id):
        try:
            usergroup = UserGroup.objects.get(id=id)
            usergroup.delete()
            return JsonResponse({'message': 'User group deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'User group does not exist'}, status=404)