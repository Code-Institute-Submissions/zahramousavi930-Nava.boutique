from django.db import models
from account_module.models import User
from main_module.models import Products


class Order(models.Model):
    userr = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.userr)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount




class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey( Products, on_delete=models.PROTECT,null=True)
    size=models.CharField(max_length=100,default='')
    color=models.CharField(max_length=100,default='')
  
    order_number = models.IntegerField(default=0)


    final_price = models.CharField(max_length=2000,null=True, blank=True)
    count = models.IntegerField(default=1)

    def get_total_price(self):
        return self.count * self.product.price


    def __str__(self):
        return str(self.order)




class order_data(models.Model):
    full_name=models.CharField(max_length=200)
    email_address=models.EmailField(max_length=300)
    phone_number=models.CharField(max_length=500)
    street_address1=models.CharField(max_length=500)
    town_or_city=models.CharField(max_length=500)
    country_state_or_location=models.CharField(max_length=500)
    post_code=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    which_order=models.ManyToManyField(OrderDetail,default=None)
    which_user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)



    def __str__(self):
        return self.email_address



