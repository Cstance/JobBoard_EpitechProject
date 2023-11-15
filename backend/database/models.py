# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):

    # Overriding create_user method to match new user
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Ensure a name, a last name and a password are provided 
        if not extra_fields.get('name'):
            raise ValueError('The name field must be set')
        if not extra_fields.get('last_name'):
            raise ValueError('The last_name field must be set')
        if not user.is_superuser and not user.has_usable_password():
            raise ValueError('A password is required')

        user.set_password(password)
        user.save(using=self._db)
        return user

    # Define the email field as the identifier field
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=256, blank=True)
    advertiser = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)

    objects = UserManager()

    # Define the email field as the identifier field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    def save(self, *args, **kwargs):
        # Ensure a name, a last name and a password are provided 
        if not self.name:
            raise ValueError('The name field must be set')
        if not self.last_name:
            raise ValueError('The last_name field must be set')
        if not self.is_superuser and not self.has_usable_password():
            raise ValueError('A password is required')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Companies(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    sector = models.CharField(max_length=64, blank=True)


    
class Advertisements(models.Model):
    title = models.CharField(max_length=128)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    salary = models.IntegerField(blank=True)
    type = models.CharField(max_length=64, blank=True)
    description = models.TextField()
    starting_date = models.DateField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    
    
class Application(models.Model):
    applicant = models.ForeignKey(Users, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisements, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)
