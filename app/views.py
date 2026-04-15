from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Publisher, Book
from django.db import models
from .filter import FilterBook

def home(request):
    return render(request, 'home.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher/publisher_list.html', {'publishers': publishers})

def book_list(request):
    books = Book.objects.all()
    book_filter = FilterBook(request.GET, queryset=Book.objects.all())
    return render(request, 'book/book_list.html', {
        'books': book_filter.qs,
        'filter': book_filter
    })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category/category_detail.html', {'category': category})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'publisher/publisher_detail.html', {'publisher': publisher})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('category_list')
    return render(request, 'category/category_create.html')

def create_author(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        bio = request.POST.get('bio')
        Author.objects.create(full_name=full_name, email=email, photo=photo, bio=bio)
        return redirect('author_list')
    return render(request, 'author/author_create.html')

def publisher_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        logo = request.FILES.get('logo')
        Publisher.objects.create(name=name, address=address, phone=phone, logo=logo)
        return redirect('publisher_list')
    return render(request, 'publisher/publisher_create.html')

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = get_object_or_404(Category, pk=request.POST.get('category'))
        author = get_object_or_404(Author, pk=request.POST.get('author'))
        publisher = get_object_or_404(Publisher, pk=request.POST.get('publisher'))
        price = request.POST.get('price')
        pages = request.POST.get('pages')
        cover = request.FILES.get('cover')
        description = request.POST.get('description')
        Book.objects.create(title=title, category=category, author=author, publisher=publisher, price=price, pages=pages, cover=cover, description=description)
        return redirect('book_list')

    context = {
        'categories': Category.objects.all(),
        'authors': Author.objects.all(),
        'publishers': Publisher.objects.all(),
    }
    return render(request, 'book/book_create.html', context)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('category_detail', pk=category.pk)
    return render(request, 'category/category_update.html', {'category': category})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.full_name = request.POST.get('full_name')
        author.email = request.POST.get('email')
        author.save()
        return redirect('author_detail', pk=author.pk)
    return render(request, 'author/author_update.html', {'author': author})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.name = request.POST.get('name')
        publisher.address = request.POST.get('address')
        publisher.phone = request.POST.get('phone')
        publisher.logo = request.FILES.get('logo')
        publisher.save()
        return redirect('publisher_detail', pk=publisher.pk)
    return render(request, 'publisher/publisher_update.html', {'publisher': publisher})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.category = get_object_or_404(Category, pk=request.POST.get('category'))
        book.author = get_object_or_404(Author, pk=request.POST.get('author'))
        book.publisher = get_object_or_404(Publisher, pk=request.POST.get('publisher'))
        book.price = request.POST.get('price')
        book.pages = request.POST.get('pages')
        book.cover = request.FILES.get('cover')
        book.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'book/book_update.html', {'book': book})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_delete.html', {'category': category})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author/author_delete.html', {'author': author})
    
def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'publisher/publisher_delete.html', {'publisher': publisher})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_delete.html', {'book': book})

def aggregate_view(request):
    book_stats = Book.objects.aggregate(
        total_books=models.Count('id'),
        total_price=models.Sum('price'),
        average_price=models.Avg('price'),
        max_price=models.Max('price'),
        min_price=models.Min('price'),
    )
    authors = Author.objects.annotate(
        num_books=models.Count('book'),
        avg_book_price=models.Avg('book__price'),
        max_book_price=models.Max('book__price'),
    )
    
    return render(request, 'stats.html', {'stats': book_stats, 'authors': authors,})




















