from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Book(models.Model):

    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=200)
    category = models.CharField(max_length=25, default="comedy")
    inventory = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f'{self.title} by {self.author}'

class Borrow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=datetime.now())
    