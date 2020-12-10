from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('authors_index', views.authors_index),
    path('books/<int:id>', views.books),
    path('authors/<int:id>', views.authors),
    path('add_author_to_curent_book', views.add_author_to_curent_book),
    path('add_book_to_current_author', views.add_book_to_current_author),
]