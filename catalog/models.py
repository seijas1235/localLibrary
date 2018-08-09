from django.db import models
from django.utils.timezone import now, timedelta, datetime
from django.contrib.auth.models import User
from random import choice
from django.utils.crypto import get_random_string
# Create your models here.


from django.urls import reverse #Used to generate urls by reversing the URL patterns

class Countries(models.Model):
    country=models.CharField(max_length=150 )

    def __str__(self):
        return self.country
    class Meta:
        ordering=['country']
        verbose_name="Pais"
        verbose_name_plural="Paices"

class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese un Genero")
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])
    
    
    def __str__(self):

        return self.name

    @property
    def books(self):
        return len(Book.objects.filter(genre_id=self.id))


    class Meta:
        ordering=['name']
        verbose_name="Tema"
        verbose_name_plural="Temas"
        
        
 
class Book(models.Model):
    """
    Modelo para creacion de un nuevo libro
    """
    title = models.CharField(max_length=200, verbose_name=("Titulo"))
    author = models.ForeignKey('Author', on_delete=models.CASCADE,  verbose_name=("Autor"))
    date_of_admission = models.DateTimeField(auto_now_add=True, verbose_name=("Fecha de Ingreso"))
    available=models.IntegerField(default=0, verbose_name=("Disponibles"))
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,  verbose_name=("Genero"))
    location=models.CharField(max_length=250,verbose_name='ubicacion')
    library=models.ForeignKey('library', verbose_name=("Biblioteca"), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    
    
    @property
    def books(self):
        return len(Book.objects.filter(author_id=self.id))

    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libros"


    def get_absolute_url(self):
      
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
        
        
import uuid 
from datetime import date

from django.contrib.auth.models import User 

class Author(models.Model):
    """
    Modelo para nuevo autor
    """
    first_name = models.CharField(max_length=100, verbose_name=("Nombres"))
    last_name = models.CharField(max_length=100, verbose_name=("Apellidos"))
    date_of_birth = models.DateField( verbose_name=("Fecha de nacimiento"))
    date_of_death = models.DateField( null=True, blank=True, verbose_name=("Fecha de muerte"))
    country=models.ForeignKey('countries',on_delete=models.CASCADE, verbose_name=("Pais"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    class Meta:
        ordering = ["first_name","last_name"]
        verbose_name="Autor"
        verbose_name_plural="Autores"
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
   
        return '{0}, {1}'.format(self.first_name,self.last_name)
   
    @property
    def books(self):
        return len(Book.objects.filter(author_id=self.id))



class State(models.Model):
    state=models.CharField(max_length=50, verbose_name='estado')
    def __str__(self):
        return self.state

class Library(models.Model):
    name=models.CharField(max_length=150, verbose_name='Bibliteca' )
    description=models.TextField(verbose_name="Descripcion")
    ubication=models.CharField(max_length=200,verbose_name="Direccion")
    latitud=models.CharField(max_length=200, verbose_name="latitud")
    longitud=models.CharField(max_length=200, verbose_name="longitud")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    seleccionado=models.BooleanField(default=False)
    def get_absolute_url(self):
        self.seleccionado=True
        return reverse('library', args=[str(self.id)])
    
   
    class Meta:
        ordering=['name']
        verbose_name="Libraria"
        verbose_name_plural="Librerias"

    def __str__(self):
        return self.name

#lend
class Loan(models.Model):

    user=models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    book=models.ForeignKey(Book, verbose_name="Libro", on_delete=models.CASCADE)
    date_of_admission=datetime.now()
    date_of_return=date_of_admission+(timedelta(days=8))
    state=models.ForeignKey(State,verbose_name="estado", on_delete=models.CASCADE)
    tokem = models.CharField(max_length=16, verbose_name='Token', default=get_random_string(length=16, allowed_chars='abcdefghj]kmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'))
    
    def get_absolute_url(self):
        return reverse('loan-detail', args=[str(self.id)])
    

    class Meta:
        verbose_name="Prestamo"
        verbose_name_plural="Prestamos"
    
    def __str__(self):
        return self.tokem



