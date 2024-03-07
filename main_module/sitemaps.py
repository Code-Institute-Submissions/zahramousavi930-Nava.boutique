from django.contrib.sitemaps import Sitemap
from .models import Products

class AccountSitemap(Sitemap):
    protocol = 'http'
    priority = '0.5' 
    changefreq = 'weekly'

    def items(self):
       
        return Products.objects.all()

    
    def location(self, obj):
        return '/products/{}/'.format(obj.pk)
