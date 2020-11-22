from rest_framework import serializers
from .models import Product, Account

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'name' , 'price', 'category']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Account
        fields = [ 'email', 'username', 'password', 'password2']
        extra_kwargs ={
            'password': {'write_only': True}
        }
    def save(self):
        account = Account(email =self.validated_data['email'],
            username =self.validated_data['username'] 
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        account.set_password(password)
        account.save()

class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username']