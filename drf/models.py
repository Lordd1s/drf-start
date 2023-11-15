from django.db import models
from django.utils import timezone


# Create your models here.
class ProposeModel(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    email = models.TextField(max_length=50, verbose_name="Почта")
    suggestion = models.TextField(max_length=200, verbose_name="Предложения")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'drf'
        ordering = ['-date', 'full_name']
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f"Предложение от {self.full_name} по дате {self.date}"


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=20)

    class Meta:
        app_label = "drf"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Категория {self.name}"


class News(models.Model):
    category = models.ManyToManyField(verbose_name="Категории", to=Category, blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    description = models.TextField(verbose_name="Подробнее", max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "drf"
        ordering = ["-timestamp", "title"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"Новость {self.title}, по категории {self.category}"
