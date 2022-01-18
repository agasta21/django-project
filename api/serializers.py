from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product,Transaction,TransactionDetail
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import serializers

class ProductSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name','testtype','code','price','created','updated']

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ['id','userid', 'totalprice', 'orderdate', 'created', 'updated']


class TransactionDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TransactionDetail
		fields = ['productid','orderquantity','transactionid','unitprice','totalprice']

