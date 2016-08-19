from rest_framework import generics
from ..models import Catalogo
from .serializers import CatalogoSerializer
from rest_framework.permissions import IsAuthenticated

class CatalogoListView(generics.ListAPIView):
	queryset = Catalogo.objects.all()
	serializer_class = CatalogoSerializer
	permission_classes = (IsAuthenticated,)

class CatalogoDetailView(generics.RetrieveAPIView):
	queryset = Catalogo.objects.all()
	serializer_class = CatalogoSerializer
	permission_classes = (IsAuthenticated,)