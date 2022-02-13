from .logic import measurements_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            variable_dto = vl.get_measurement(id)
            variable = serializers.serialize('json', [variable_dto,])
            return HttpResponse(variable, 'application/json')
        else:
            variables_dto = vl.get_measurements()
            variables = serializers.serialize('json', variables_dto)
            return HttpResponse(variables, 'application/json')

    if request.method == 'POST':
        variable_dto = vl.create_measurement(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        variable_dto = vl.get_measurement(pk)
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

    if request.method == 'PUT':
        variable_dto = vl.update_measurement(pk, json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

    if request.method == 'DELETE':
        variable_dto = vl.delete_measurement(pk)
        return HttpResponse(variable_dto)