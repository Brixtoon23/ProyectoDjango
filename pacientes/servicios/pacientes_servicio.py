from pacientes.serializers import PacienteSerializer
from ..models import Paciente

def obtener_pacientes():
    return Paciente.objects.all()

def obtener_paciente_por_id(paciente_id):
    return Paciente.objects.filter(id=paciente_id).first()

def crear_paciente(datos):
    serializer = PacienteSerializer(data=datos)
    if serializer.is_valid():
        return serializer.save()
    return None


def actualizar_paciente(paciente, datos):
    for key, value in datos.items():
        setattr(paciente, key, value)
    paciente.save()
    return paciente

def eliminar_paciente(paciente):
    paciente.delete()
