from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('library/<int:pk>', views.BooksDetailView.as_view(), name='library'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('genre/', views.GenreListView.as_view(), name='genre'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),  
    path('loan/', views.LoanListView.as_view(), name='loan'),
    path('loan/<int:pk>', views.LoanDetailView.as_view(), name='loan-detail'),
]
# urls para crear/ editar / eliminar autores 

urlpatterns += [ 
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# urls para crear, editar y eliminar libros
urlpatterns += [  
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]


#url para crear editar y eliminar temas
urlpatterns += [  
    path('genre/create/', views.GenreCreate.as_view(), name='genre_create'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
]

#url para crear y editar prestamos
urlpatterns += [ 
    path('loan/create/', views.LoanCreate.as_view(), name='loan_create'), 
    path('loan/<int:pk>/update/', views.LoanUpdate.as_view(), name='loan_update'),
]