from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=35, verbose_name="Номер телефона", help_text="Укажите номер телефона", **NULLABLE)
    avatar = models.ImageField(upload_to="media/avatars/", verbose_name="Аватар", help_text="Загрузите изображение", **NULLABLE)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Укажите страну", **NULLABLE)
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
