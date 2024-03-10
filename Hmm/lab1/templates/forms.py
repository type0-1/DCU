# forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import *
from django.db import transaction
from datetime import datetime

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["year", "author", "price", "title", "synopsis", "category"]
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        year = data.get("year")
        inventory = data.get("inventory")
        current_year = datetime.now().year

        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("A book of this title already exists")

        if year > current_year:
            raise forms.ValidationError("This year is invalid")
        
        if inventory == 0:
            raise forms.ValidationError("This book isn't available, wait until restock!")
        
        return data

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["year", "author", "price", "title", "synopsis", "category"]