from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='publishers/')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='books/')
    description = models.TextField()

    def __str__(self):
        return self.title
