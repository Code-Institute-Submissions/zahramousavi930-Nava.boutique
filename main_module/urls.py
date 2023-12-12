
from django.urls import path
from . import views
urlpatterns = [
path('',views.Home_page.as_view(), name='home_pgae' ),
    path('products/<str:slug>/<int:pk>', views.Products.as_view(), name='products_pgae'),
    path('add_comments', views.add_comments_part, name='add_comments'),
]
