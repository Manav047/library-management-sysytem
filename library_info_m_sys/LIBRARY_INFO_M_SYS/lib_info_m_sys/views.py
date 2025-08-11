from operator import truediv

from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .models import Book

def home(request):
    return render(request, 'home.html', context={"current_tab":"home"})

def readers(request):
    return render(request, 'readers.html', context={"current_tab":"readers"})

def books(request):
    return render(request, 'books.html', context={"current_tab":"books"})

def bag(request):
    return render(request, 'bag.html', context={"current_tab":"bag"})

def return_books(request):
    return render(request, 'return_books.html', context={"current_tab":"return_books"})

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, 'welcome.html', context={'student_name':student_name})


def readers_tab(request):
    readers=reader.objects.all()
    return render(request, 'readers.html', context={"current_tab":"readers",'readers':readers})

def save_readers(request):
    reader_item =readers(reference_id=request.POST['readers_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST['address'],
                         active=True
                         )
    reader_item.save()
    return redirect('/readers')
def manage_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'manage_books.html', {'books': books})
def update_book_quantity(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            book.quantity += 1  # Increment quantity
        elif action == 'subtract' and book.quantity > 0:
            book.quantity -= 1  # Decrement quantity if greater than 0
        book.save()
    return redirect('manage_books')  # Redirect back to the manage books page