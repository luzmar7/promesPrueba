from rest_framework import serializers
from .models import Medico, OrdenLaboratorio

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenLaboratorio
        fields = '__all__'