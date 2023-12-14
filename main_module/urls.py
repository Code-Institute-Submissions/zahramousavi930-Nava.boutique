from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home_page.as_view(), name='home_pgae' ),
    path('all',views.all_peoducts.as_view(), name='all_products_pgae' ),
    path('products/<str:slug>/<int:pk>',views.Products.as_view(), name='products_pgae' ),
    path('add_comments',views.add_comments_part,name='add_comments'),
    path('category/<int:id>',views.category.as_view(),name='category_product'),
    path('newsteller',views.newsteller,name='news_teller'),
    path('removenewsteller',views.remove_news_teller,name='remove_news_teller'),
    path('contact',views.contact_with_us.as_view(),name='contact_with_us'),
    path('save-contact',views.save_contact_us,name='save_contact'),
    path('addtocart',views.addtocart,name='add_to_cart'),
    path('search',views.search,name='search'),




]

