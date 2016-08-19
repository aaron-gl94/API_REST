from rest_framework import generics
from ..models import Catalogo
from .serializers import CatalogoSerializer

class CatalogoListView(generics.ListAPIView):
	queryset = Catalogo.objects.all()
	serializer_class = CatalogoSerializer
class CatalogoDetailView(generics.RetrieveAPIView):
	queryset = Catalogo.objects.all()
	serializer_class = CatalogoSerializer