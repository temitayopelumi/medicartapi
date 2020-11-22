from django.urls import path

from .views import api_product, Productlist, registration_view, UpdateProduct,addProduct,ProductListView,update_account_view,account_properties_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'medicartapp'

urlpatterns = [
    path('product/<str:pk>/', api_product, name='products'),
    path('products/', Productlist, name='list'),
    path('updateproduct/<str:pk>/', UpdateProduct, name='updateproduct'),
    path('createproduct/', addProduct, name='addproduct'),

    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('list/', ProductListView.as_view(), name="list"),

    path('profile/', account_properties_view, name='profile'),
    path('profile/update/', update_account_view, name='updateprofile')
]