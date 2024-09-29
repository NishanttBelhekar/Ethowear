from django.db import models
from .category import Category
from .type import Type
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=50)
    sizes_choice =(
    ("1","L"),
    ("2","M"),
    ("3","S")
)
    sizes = models.CharField(max_length=50, blank=True, null = True, choices = sizes_choice, default='1')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1' )
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default='1' )
    productinfo = models.TextField(max_length=1200, default=' ', null=True, blank=True)
    description = models.TextField(max_length=1200, default=' ', null=True, blank=True)
    image = models.ImageField(upload_to='upload/products/')

    
    @staticmethod 
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)
        
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
            
    def get_all_products_by_typeid(type_id):
        if type_id:
            return Product.objects.filter(type = type_id)
        else:
            return Product.get_all_products();

