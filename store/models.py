from django.db import models

# Create your models here.
# read about django Model field types

########### How define many-to-many relationship ########
    
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    pass

class Product(models.Model):
    title = models.CharField(max_length=255) #varchar(255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    promotions = models.ManyToManyField(Promotion,related_name='products')# products is name of the attr in Promotion respectively if you doesnt set related name the default is product_set


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B','Bronze'),
        ('S','Silver'),
        ('G','Green'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    # use choice field:
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default='B')


# Exercice
    
class Order(models.Model):
    PENDING = 'Pending'
    COMPLETE = 'Complete'
    FAILED = 'Failed'

    CHOICES = [
        (PENDING[0],PENDING),
        (COMPLETE[0],COMPLETE),
        (FAILED[0],FAILED)
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=CHOICES,default=PENDING[0]
    )


# Create one to one relationship
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # specify  parent
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    """
    CASCADE: Delete related objects when the referenced object is deleted.
    PROTECT: Prevent deletion of the referenced object if related objects exist.
    SET_NULL: Set the foreign key or one-to-one relationship to NULL when the referenced object is deleted.
    SET_DEFAULT: Set the foreign key or one-to-one relationship to its default value when the referenced object is deleted.
    SET(): Set the foreign key or one-to-one relationship to a custom value when the referenced object is deleted.
    DO_NOTHING: Do nothing when the referenced object is deleted.
    RESTRICT: Prevent deletion of the referenced object at the database level.
    
    """

    # if we doesnt set primary_key to True the relationship will be one-to-many




# Create one-to-many relationship:
# Just use ForeignKey function of models and not set primary key
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)    


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()




