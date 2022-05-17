import django
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from crud.models import Business
from crud.serializers import BusinessSerializer

# Create your views here.

def start(request):
    return render(request, 'index.html')

@csrf_exempt
def enterprise_api(request, id = 0):
  if request.method == 'GET':
    enterprises = Business.objects.all()
    enterprises_serializer = BusinessSerializer(enterprises, many=True)
    return JsonResponse(enterprises_serializer.data, safe=False)

  elif request.method == 'POST':
    enterprise_data = JSONParser().parse(request)
    enterprises_serializer = BusinessSerializer(data=enterprise_data)

    if enterprises_serializer.is_valid():
      enterprises_serializer.save()
      return JsonResponse("Enterprise created successfully", status=201, safe=False)
    else :
      return JsonResponse(enterprises_serializer.errors, status=400, safe=False)

  elif request.method == 'PUT':
    enterprise_data = JSONParser().parse(request)
    enterprise = Business.objects.get(BusinessId = enterprise_data['BusinessId'])
    enterprises_serializer = BusinessSerializer(enterprise, data=enterprise_data)
    if enterprises_serializer.is_valid():
      enterprises_serializer.save()
      return JsonResponse("Enterprise updated successfully", status=201, safe=False)
    else :
      return JsonResponse(enterprises_serializer.errors, status=400, safe=False)

  elif request.method == 'DELETE':
    Business.objects.get(BusinessId = id).delete()
    return JsonResponse("Enterprise deleted successfully", status=200, safe=False)
