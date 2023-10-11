from django.db import models
from django.utils import timezone


# Create your models here.
class ProposeModel(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    email = models.TextField(max_length=50, verbose_name="Почта")
    suggestion = models.TextField(max_length=200, verbose_name="Предложения")
    date = models.TextField(max_length=20, verbose_name="Дата")

    class Meta:
        app_label = 'drf'
        ordering = ['-date', 'full_name']
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f"Предложение от {self.full_name} по дате {self.date}"
