from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from .models import Book, Author,  Genre, Library,Loan
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import  login_required

@login_required
def index(request):
    """
    VISTA DE PAGINA PRINCIPAL  INDEX
    """
    num_books=Book.objects.all().count()
    num_authors=Author.objects.count() 
    library_list=Library.objects.all()
    
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
 
   
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors,
            'num_visits':num_visits,'library_list':library_list},
    )



class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """

    model = Book
    paginate_by = 5

    def get_queryset(self):
        print(self.request.GET.get('local'))
        return self.model.objects.filter(library=Library.objects.get(pk=self.request.GET.get('local')))


class BooksDetailView(generic.DetailView):
    """
    Generic class-based view for a list of books.
    """
    model = Library


class BookDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Book

class AuthorListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = Author
    paginate_by = 5 
    model = Author
    


class AuthorDetailView(generic.DetailView):
    """
    Generic class-based detail view for an author.
    """

class LoanListView(generic.ListView):
    """
    Generic class-based list view for a list of genre.
    """
    model = Loan
    
    if Loan.user == User:
        paginate_by = 3


class LoanDetailView(generic.DetailView):
    """
    Generic class-based detail view for an genre.
    """
    model = Loan


class GenreListView(generic.ListView):
    """
    Generic class-based list view for a list of genre.
    """
    model = Genre
    paginate_by = 5 


class GenreDetailView(generic.DetailView):
    """
    Generic class-based detail view for an genre.
    """
    model = Genre

   
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book,Loan



class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    permission_required = 'catalog.can_mark_returned'

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'
    

class UserCreate(CreateView):
    model = User
    fields = '__all__'
     

from django.http import JsonResponse

class LoanCreate(generic.CreateView):
    model = Loan
    fields = '__all__'
    success_url = reverse_lazy('loan')



     
class LoanUpdate(PermissionRequiredMixin, UpdateView):
    model = Loan
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('loan')


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    

class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'


class GenreCreate(PermissionRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genre')
    permission_required = 'catalog.can_mark_returned'

class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genre')
    permission_required = 'catalog.can_mark_returned'

class GenreDelete(PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy('genre')
    permission_required = 'catalog.can_mark_returned'

