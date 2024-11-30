from django.db import models
from django.contrib.auth.models import User


class FoodType(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Ovqat turi")

    class Meta:
        verbose_name = "Ovqat turi"
        verbose_name_plural = "Ovqat turlari"
        ordering = ['nomi']

    def __str__(self):
        return self.nomi


class Food(models.Model):
    food_type = models.ForeignKey(
        FoodType, 
        on_delete=models.CASCADE, 
        related_name='foods',
        verbose_name="Ovqat turi"
    )
    nomi = models.CharField(max_length=100, verbose_name="Ovqat nomi")
    tarkibi = models.TextField(verbose_name="Ovqat tarkibi")
    narxi = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Narxi"
    )
    views = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")

    class Meta:
        verbose_name = "Ovqat"
        verbose_name_plural = "Ovqatlar"
        ordering = ['nomi']

    def __str__(self):
        return self.nomi


class Comment(models.Model):
    text = models.TextField(verbose_name="Izoh")
    food = models.ForeignKey(
        Food, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name="Ovqat"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Foydalanuvchi"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created']

    def __str__(self):
        return f"{self.author.username}: {self.text[:20]}"
