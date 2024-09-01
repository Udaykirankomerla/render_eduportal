from django import forms
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



# Create your models here.
class UserManager(BaseUserManager):
    def createuser(self,firstname,lastname,username,email,password=None):
        if not email:
            raise ValueError('enter the valid email')
        if not username:
            raise ValueError('enter the valid username')
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email)
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,firstname,lastname,username,email,password=None):
        user=self.createuser(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email),
            password=password
            
        )
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email= models.EmailField(max_length=50,unique=True)
    


    datejoined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname']
    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email} - {self.firstname} - {self.lastname} - {self.username}"
    
    def has_module_permission(self,app_label):
        return True
