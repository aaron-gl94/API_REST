from django.db import models

class Catalogo(models.Model):
	postre = models.CharField(max_length=140)
	precio = models.TextField()
	vigencia = models.DateTimeField(auto_now=true)
	def __str__(self):
		return self.postre
