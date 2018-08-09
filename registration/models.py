from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from catalog.models import Loan
# Create your models here.

class Departmento(models.Model):
    title=models.CharField(max_length=75, verbose_name='Departamento')

    def __str__(self):
        return self.title

class Municipio(models.Model):
    depto=models.ForeignKey('Departmento', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Municipio')

    def __str__(self):
        return self.title

class Escolaridad(models.Model):
    title=models.CharField(max_length=75, verbose_name='Escolaridad')
    def __str__(self):
        return self.title

class Genero(models.Model):
    title=models.CharField(max_length=50, verbose_name='Genero')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', null = True, blank=True)
    cui = models.CharField(max_length=13, verbose_name='DPI')
    direccion = models.CharField(max_length=250 )
    zona=models.IntegerField(verbose_name="Zona",null=True)
    date_of_birth = models.DateField( verbose_name="Fecha de nacimiento", null=True)
    municipio=models.ForeignKey('Municipio', on_delete=models.CASCADE, verbose_name='Municipio',null=True )
    escolaridad=models.ForeignKey('Escolaridad', verbose_name='Escolaridad', on_delete=models.CASCADE,null=True )
    genre=models.ForeignKey('Genero',on_delete=models.CASCADE, verbose_name="Genero",null=True)
    colegio=models.CharField(max_length=250, verbose_name="Institucion Educativa", null=True)
    
    @property
    def loans(self):
        return len(Loan.objects.filter(user=self.user, state__lte= 2))