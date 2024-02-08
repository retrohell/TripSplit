import json
from django.http import JsonResponse
from django.db import IntegrityError
from ..models import Group, Guest, UserGroup
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt

def createUserGroup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            group = UserGroup.objects.create(
                guest_id = Guest.objects.get(id=data['guest_id']),
                group_id = Group.objects.get(id=data['group_id']),
            )
            group.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating group'}, status=400)
        
def getUserGroup(request, id):
    if request.method == 'GET':
        group = UserGroup.objects.get(id=id)
        group = serializers.serialize('json', [group,])
        json_data = json.loads(group)
        return JsonResponse(json_data, status=200, safe=False)