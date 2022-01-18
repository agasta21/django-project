from django.db import models

# Create your models here.
class Transaction(models.Model):
    userid = models.DecimalField(max_digits=9, decimal_places=0) 
    totalprice = models.DecimalField(max_digits=20, decimal_places=0)
    orderdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return 'ID : ' + str(self.id)

class TransactionDetail(models.Model):
    transactionid = models.DecimalField(max_digits=9, decimal_places=0)
    productid = models.DecimalField(max_digits=9, decimal_places=0)
    orderquantity = models.DecimalField(max_digits=20, decimal_places=0)
    unitprice = models.DecimalField(max_digits=20, decimal_places=0)
    totalprice = models.DecimalField(max_digits=20, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

   

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'ID : ' + str(self.id)



class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    testtype = models.CharField(max_length=255)
    


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
