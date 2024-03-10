from django.urls import path
from . import views
from .forms import * 

urlpatterns = [
   path('', views.index, name="index"),
   path('contact', views.contact, name="contact"),
   path('variable', views.variable, name="variable"),
   path('add', views.add, name="add"),
   path('random', views.randomnumber, name="random"),
   path('loop', views.forLoop, name="for_loop"),
   path('numbers', views.ex2, name="numbers"),
   path('fizzbuzz', views.fizzbuzz, name="fizzbuzz"),
   path('books', views.view_all_books, name="all_books"),
   path('books/<int:bookid>', views.single_book, name="single_book"),
   path('books/year/<int:year>', views.by_year, name="all_books"),
   path('books/category/<str:category>', views.by_category, name="all_books"),
   path('books/category/<str:category>/year/<int:year>', views.category_and_year, name="all_books"),
   path('register/', views.UserSignupView.as_view(), name="user_signup"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
   path('logout/', views.logout_user, name="logout"),
   path('books/add',views.add_book, name="add_book"),
   path('edit_book/<int:bookid>',views.update_book, name="update_book"),
   path('checkout/<int:bookid>',views.checkout_book, name="checkout"),
]