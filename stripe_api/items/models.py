from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название товара'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.PositiveIntegerField(
        verbose_name='Стоимость'
    )
