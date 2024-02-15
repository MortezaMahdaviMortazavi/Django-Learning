from django.db import models
from django.contrib.contenttypes.models import ContentType # for create generic relationships 

# from store.models import Product
# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)

    ### identifying the object is refer to
    # product = models.ForeignKey(Product)
    ### this error happened if you want to resolve it should import store models which is different app and its not efficient to import other apps

    # to solve it we need these:
    # Type(product , video , article)
    # ID for finding record
    product = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    
