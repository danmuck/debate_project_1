from django.urls import path
from .views import (
    product_list_view,
    product_create_view,
    product_delete_view,
    product_detail_view,
    render_initial_data
)

app_name = 'products'
urlpatterns = [
#products[yt]
    path('', product_list_view, name='products'),
    path('create/', product_create_view, name='products'),
    path('<int:product_id>/', product_detail_view, name='product'),
    path('<int:product_id>/edit/', render_initial_data, name='render'),
    path('<int:product_id>/delete/', product_delete_view, name='delete'),
    
]
