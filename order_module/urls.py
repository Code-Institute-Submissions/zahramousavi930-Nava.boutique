from django.urls import path
from . import views




urlpatterns = [
    path('shoping-cart',views.Shoping_cart.as_view(),name='shoping_cart'),
    path('stripe',views.stripe_webhook,name='stripe'),
    path('detail-cart/<int:pk>',views.detailcart,name='detailcart'),
    path('addtocart',views.addtocart,name='add_to_cart'),
    path('modify_order_detail',views.modify_order_detail,name='modify_order_detail'),
]