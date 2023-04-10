from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:author_id>/', views.quotes_by_author, name='quotes_by_author'),
]
