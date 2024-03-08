from django.contrib import admin
from . import models
# Register your models here.

class admin_product(admin.ModelAdmin):
    list_display = ('name','category','price','discount_price','discount')
    list_editable = ('price','discount_price','discount')


class admin_gift(admin.ModelAdmin):
    list_display = ('name','category','price','discount_price','discount')
    list_editable = ('price','discount_price','discount')

admin.site.register(models.Category)
admin.site.register(models.Products,admin_product)
admin.site.register(models.News_teller)
admin.site.register(models.add_comments)
admin.site.register(models.contact_with_us)
admin.site.register(models.contact)
