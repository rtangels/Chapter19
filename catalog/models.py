from django.db import models

NULLABLE={'null':True, 'blank':True}

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    discription = models.TextField(**NULLABLE)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
class Product (models.Model):
    name = models.CharField(max_length=100, verbose_name='Название' )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name ='Категория')
    discription = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to= 'catalog/', null=True, blank=True, verbose_name='Фото')
    price =models.IntegerField(null=True, blank=True, verbose_name='Цена')
    date_of_сreation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_сhange = models.DateTimeField(**NULLABLE, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} ({self.category}): {self.price}'

    class Meta:
        verbose_name='продукт'
        verbose_name_plural = 'продукты'

