from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('categories/', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:pk>/', category_update, name='category_update'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),

    path('authors/', author_list, name='author_list'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
    path('author/create/', create_author, name='create_author'),
    path('author/update/<int:pk>/', author_update, name='author_update'),
    path('author/delete/<int:pk>/', author_delete, name='author_delete'),

    path('publishers/', publisher_list, name='publisher_list'),
    path('publisher/<int:pk>/', publisher_detail, name='publisher_detail'),
    path('publisher/create/', publisher_create, name='publisher_create'),
    path('publisher/update/<int:pk>/', publisher_update, name='publisher_update'),
    path('publisher/delete/<int:pk>/', publisher_delete, name='publisher_delete'),

    path('books/', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/create/', create_book, name='create_book'),
    path('book/update/<int:pk>/', book_update, name='book_update'),
    path('book/delete/<int:pk>/', book_delete, name='book_delete'),

    path('stats/', aggregate_view, name='stats'),

    path('change_password/', change_pass_view, name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]