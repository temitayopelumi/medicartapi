from django.urls import path

from .views import api_product, Productlist, registration_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'medicartapp'

urlpatterns = [
    path('product/<str:pk>/', api_product, name='products'),
    path('products/', Productlist, name='list'),

    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login')
]