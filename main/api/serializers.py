from rest_framework import serializers
from ..models import Catalogo  

class CatalogoSerializer(serializers.ModelSerializer):
        class Meta:
        	model = Catalogo 
        	fields = ('id','postre','precio','vigencia')

