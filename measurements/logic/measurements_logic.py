from urllib import response
from ..models import Measurement

def get_measurements():
    variables = Measurement.objects.all()
    return variables

def get_measurement(var_pk):
    variable = Measurement.objects.get(pk=var_pk)
    return variable

def update_measurement(var_pk, new_var):
    variable = get_measurement(var_pk)
    variable.variable_id =new_var["variable_id"]
    variable.value =new_var["value"]
    variable.unit =new_var["unit"]
    variable.place =new_var["place"]
    variable.save()
    return variable

def create_measurement(var):
    variable = Measurement(variable_id = var["variable_id"], value = var["value"],
        unit = var["unit"],
        place = var["place"]
       )
    variable.save()
    return variable

def delete_measurement(var_pk):
    variable = get_measurement(var_pk)
    print(variable)
    response = u'Successful delete route {}'.format(variable)
    variable.delete()
    return response