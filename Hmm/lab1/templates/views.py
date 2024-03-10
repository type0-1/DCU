from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from datetime import *
from .models import *
from .forms import *
import random

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class UserLoginView(LoginView):
    template_name='login.html'

def logout_user(request):
    logout(request)
    return redirect("/")

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def variable(request):
    x = 5
    return render(request, 'variable.html', {'x':x})

def add(request):
    x = 5
    y = 7
    return render(request, 'add.html', {'x':x, 'y':y, 'z':x+y})

def randomnumber(request):
   x = random.randint(0,100) # generate a random number between 0 and 100
   return render(request,'random.html',{'x':x})

def forLoop(request):
    list1 = ["a", "b", "c", "d"]
    return render(request, 'for_loop.html', {'letters':list1})

def ex2(request):
    numbers = [i for i in range(1, 31)]
    return render(request, 'numbers.html', {'numbers':numbers})

def fizzbuzz(request):
    numbers = list(range(1, 101))
    return render(request, 'fizzbuzz.html', {'numbers':numbers})

def view_all_books(request):
    all_books = Book.objects.all() # Get all book objects
    return render(request, 'all_books.html', {'books':all_books})

def single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid) # Get the object based off the id provided the parameter and pass it to the template rendered
    return render(request, 'single_book.html', {'book':single_book})

def by_year(request, year):
    year_specific_books = Book.objects.filter(year=year)
    return render(request, "all_books.html", {'books':year_specific_books})

def by_category(request, category):
    category_specific_books = Book.objects.filter(category=category)
    return render(request, "all_books.html", {'books':category_specific_books})

def category_and_year(request, category, year):
    category_and_year_books = Book.objects.filter(category=category, year=year)
    return render(request, "all_books.html", {'books':category_and_year_books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return render(request, 'created.html', {'book':book})
        else:
            return render(request, 'add_book.html', {'form':form})
    else:
        form = BookForm()
    return render(request, "add_book.html", {'form':form})

def update_book(request, bookid):
    book = get_object_or_404(Book, id=bookid)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return render(request, 'update_created.html', {'book':book})
        else:
            return render(request, 'update_book.html', {'form':form})
    else:
        form = BookForm(instance=book)
    return render(request, "update_book.html", {'form':form})

def checkout_book(request, bookid):
    book = get_object_or_404(Book, id=bookid)
    if request.method == "POST":
        form = CheckoutForm(request.POST, instance=book)
        if form.is_valid():
            checkout = form.save(commit=False)
            if book.inventory <= 0:
                return render(request, "out_of_stock.html");
            Borrow.objects.create(user=request.user, book=book, date=datetime.now()+timedelta(days=7))
            book.inventory -= 1
            book.save()
            checkout.save()
            return render(request, 'successful_checkout.html', {'book':book})
        else:
            return render(request, 'checkout.html', {'form':form})
    else:
        form = CheckoutForm(instance=book)
    return render(request, "checkout.html", {'form':form})