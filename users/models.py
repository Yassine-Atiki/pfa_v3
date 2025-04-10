from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator,MaxLengthValidator,MinLengthValidator

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')
        if not username:
            raise ValueError('Les utilisateurs doivent avoir un nom d\'utilisateur')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    CIN = models.CharField(max_length=8, unique=True, validators=[MinLengthValidator(8), MaxLengthValidator(8)])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    
    # Champs obligatoires pour AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'  # Champ utilisé comme identifiant
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # Champs requis lors de la création d'un utilisateur
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class ProprietaireVE(Users):
    pass

class Fournisseur(Users):
    pass

class Administrateur(Users):
    pass

# Create your models here.