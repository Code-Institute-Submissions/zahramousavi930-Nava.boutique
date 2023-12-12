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





class add_comments(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return str(self.user)




class contact_with_us(models.Model):
    email=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    about_us=models.TextField(max_length=600)

    def __str__(self):
        return self.email




class contact(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=200)
    text=models.TextField(max_length=500)

    def __str__(self):
        return self.email
