from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, Countries,Loan,State, Library
from registration.models import Municipio, Departmento, Genero, Escolaridad

admin.site.register(Municipio)
admin.site.register(Departmento)
admin.site.register(Genero)
admin.site.register(Escolaridad)



admin.site.register(Genre)
admin.site.register(Countries)

class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_admission','date_of_return','tokem')
    list_display = ('tokem','user','book', 'date_of_admission', 'date_of_return','state')
    fields = ['tokem','user','book', 'date_of_admission', 'date_of_return','state']

admin.site.register(Library)
admin.site.register(Loan,LoanAdmin)
#admin.site.register(State)

class BooksInline(admin.TabularInline):
    """
    Defines format of inline book insertion (used in AuthorAdmin)
    """
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Administration object for Author models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('first_name','last_name', 'date_of_birth', 'date_of_death','country')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death','country')]




class BookAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'genre','date_of_admission','available','location')


admin.site.register(Book, BookAdmin)
