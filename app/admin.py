from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Category, Author, Publisher, Book


    
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)

admin.site.unregister(Group)
admin.site.unregister(User)