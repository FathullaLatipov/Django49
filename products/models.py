from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    product_title = models.CharField(max_length=50, verbose_name=_('product_title'), help_text='Тут добавьте названия товара')
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_count = models.IntegerField()
    product_descriptions = RichTextField()
    product_image = models.FileField(upload_to='product_images')
    product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

# Таблица для корзины
class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    user_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'User cart'
        verbose_name_plural = 'User carts'

