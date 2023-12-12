from django.db import models
from account_module.models import User
# Create your models here.




class Category(models.Model):
    image=models.ImageField(upload_to='category')
    parent=models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    categoryy=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.categoryy




class Products(models.Model):
    name=models.CharField(max_length=300)
    slug=models.CharField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price=models.IntegerField()
    size=models.IntegerField()
    description=models.TextField(max_length=9000)
    image=models.ImageField(upload_to='products')
    favorit=models.ManyToManyField(User,null=True,blank=True)

    discount=models.IntegerField(null=True,default=0)
    discount_price=models.IntegerField(null=True,default=0)


    def __str__(self):
        return self.name




class News_teller(models.Model):
    email=models.EmailField(max_length=200)

    def __str__(self):
        return self.email
