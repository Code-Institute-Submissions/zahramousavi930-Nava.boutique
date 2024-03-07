from django.contrib.sitemaps import Sitemap
from accout_module.models import Products

class AccountSitemap(Sitemap):
    protocol = 'http'
    priority = '0.5' 
    changefreq = 'weekly'

    def items(self):
       
        return Products.objects.all()

    def lastmod(self, obj):
        
        return obj.updated
