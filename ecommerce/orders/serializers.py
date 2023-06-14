from .models import Voluntarios,Delegados,Proyectos,Categorias,Seguimiento,ZonasRecuperadas

from rest_framework.serializers import ModelSerializer 
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers

class VoluntarioSerializer(ModelSerializer):
    
    class Meta:
        model = Categorias
        fields = '__all__'

class DelegadoSerializer(ModelSerializer):
    class Meta:
        model = Delegados
        fields = '__all__'    

class SeguimientoSerializer(ModelSerializer):
    IDVoluntario=VoluntarioSerializer(many=False)
    IDDelegado=DelegadoSerializer(many=False)
    class Meta:
        model = Seguimiento
        fields = '__all__' 

    
