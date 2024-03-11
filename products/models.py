from django.db import models


# python manage.py makemigrations
# Таблица для категорий
class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'


#  Таблица для продуктов
class ProductModel(models.Model):
    product_title = models.CharField(max_length=50, help_text='Тут добавьте названия товара')
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_count = models.IntegerField()
    product_descriptions = models.TextField()
    product_image = models.FileField(upload_to='product_images')
    product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

