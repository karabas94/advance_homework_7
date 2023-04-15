from django.urls import path
from .views import BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_form'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/<int:pk>/', views.store_detail, name='store_detail'),
    path('reminder/', views.reminder, name='reminder'),
    path('reminder/success/', views.success, name='success'),
]
