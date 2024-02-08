import json
from django.http import JsonResponse
from django.db import IntegrityError
from ..models import Group
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def createGroup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            group = Group.objects.create(
                name = data['name']
            )
            group.save()
            return JsonResponse(data, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'error': 'Error creating expense'}, status=400)

def getGroup(request, id):
    if request.method == 'GET':
        group = Group.objects.get(id=id)
        group = serializers.serialize('json', [group,])
        json_data = json.loads(group)
        return JsonResponse(json_data, status=200, safe=False)