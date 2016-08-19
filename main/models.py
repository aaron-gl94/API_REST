from django.db import models

class Catalogo(models.Model): 
	postre = models.CharField(max_length=140)
	precio = models.CharField(max_length=10)
	vigencia = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.postre
