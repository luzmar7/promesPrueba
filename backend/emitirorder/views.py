from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Medico, OrdenLaboratorio
from .serializers import MedicoSerializer, OrdenSerializer

class ListaMedico(APIView):
    def get(self, request):
        medico = Medico.objects.all()[:20]
        data = MedicoSerializer(medico, many=True).data
        return Response(data)

class IngresarOrden(APIView):
    def post(self, request, id_medico):
            fecha = request.data.get("fecha")
            examen = request.data.get("examen")
            data = {'medico': id_medico, 'fecha': fecha, 'examen': examen}
            serializer =OrdenSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
