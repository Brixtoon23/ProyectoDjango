from rest_framework import viewsets
from rest_framework.response import Response  # <-- Importación añadida
from .models import Paciente
from .serializers import PacienteSerializer
from .servicios.pacientes_servicio import *

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = obtener_pacientes()
    serializer_class = PacienteSerializer

    def retrieve(self, request, *args, **kwargs):
        paciente = obtener_paciente_por_id(kwargs['pk'])
        if paciente:
            serializer = self.get_serializer(paciente)
            return Response(serializer.data)
        return Response({"error": "Paciente no encontrado"}, status=404)

    def create(self, request, *args, **kwargs):
        paciente = crear_paciente(request.data)
        serializer = self.get_serializer(paciente)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        paciente = obtener_paciente_por_id(kwargs['pk'])
        if not paciente:
            return Response({"error": "Paciente no encontrado"}, status=404)
        paciente = actualizar_paciente(paciente, request.data)
        serializer = self.get_serializer(paciente)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        paciente = obtener_paciente_por_id(kwargs['pk'])
        if not paciente:
            return Response({"error": "Paciente no encontrado"}, status=404)
        eliminar_paciente(paciente)
        return Response(status=204)
