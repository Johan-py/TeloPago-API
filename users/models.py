from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, carnet, password=None, **extra_fields):
        if not carnet:
            raise ValueError('El número de carnet es obligatorio')
        user = self.model(carnet=carnet, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, carnet, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(carnet, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    carnet = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'carnet'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'fecha_nacimiento']

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.carnet}"
