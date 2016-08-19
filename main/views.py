from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Catalogo
from django.utils.decorators import method_decorator

class HomeView(View):
	def get(self,request):
		template_name = 'catalogo/home.html'
		lista = Catalogo.objects.all().order_by('postre')
		context = {
			'lista':lista
		}
		return render(request,template_name,context)
	

