from django.db import models
from apps.default.models import Empresa

'''
	SUBCLASSE DE ESCOLA
'''
class Escola(models.Model):
	id_escola = models.AutoField(primary_key=True)
	id_empresa = models.OneToOneField(Empresa, on_delete = models.CASCADE,related_name='escola_name')
	
	def __str__(self):
		return self.id_empresa.nomefantasia
	def __unicode__(self):
		return unicode(self.id_empresa.nomefantasia)