from django.db import models
from django.contrib.auth.models import User

#Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     city = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name



class Product(models.Model):
    CATEGORY = (
        ('Baby and Child health', 'Baby and Child health'),
        ('Treatments and Medicaments','Treatments and Medicaments'),
        ('Treatments and Medicaments','Treatments and Medicaments'),
        ('First Aid','First Aid'),
        ('Sexual Wellbeing', 'Sexual Wellbeing', ),
        ('Personal Care', 'Personal Care'),

    )

    name =  models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url =self.image.url
        except:
            url = ''
        return url

# class Order(models.Model):
#     customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, blank=True)
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     date_created= models.DateTimeField(auto_now_add=True, null=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return str(self.id)

# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
#     quantity = models.IntegerField(default=0, null=True, blank=True)


# class ShippingAddress(models.Model):
#     customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     Order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city  = models.CharField(max_length=200, null=False)
#     state  = models.CharField(max_length=200, null=False)
    
#     def __str__(self):
#         return self.address


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
