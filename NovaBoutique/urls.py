from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from main_module.sitemaps import AccountSitemap
from django.views.generic import TemplateView

sitemaps = {
    'products': AccountSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account_module.urls')),
    path('', include('main_module.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain'), name="robots.txt"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
