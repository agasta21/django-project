from .serializers import ProductSerializer, TransactionSerializer, TransactionDetailSerializer
from .models import Product, Transaction, TransactionDetail
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
import json


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class TransactionViewSet(viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def create(self, request, *args, **kwargs):
    	totalprice = 0
    	i = 0
    	if isinstance(request.data, list) is not True :
    		return Response({"detail":"Post data is not a list or array"})

    	for row in request.data :

    		try:
    		    querysetProduct = Product.objects.get(id=int(row['productid']))
    		except :
    			return Response({"detail": "Product id "+str(row['productid'])+" not found"})

	    	serializerProduct = ProductSerializer(querysetProduct)
	    	request.data[i]['totalprice'] = int(serializerProduct.data["price"]) * int(row['orderquantity'])
	    	totalprice += request.data[i]['totalprice']
	    	request.data[i]['unitprice'] = serializerProduct.data["price"]
	    	i = i+1

    	dataTransaction={"userid":request.user.pk,"totalprice":totalprice}
    	serializer = TransactionSerializer(data=dataTransaction)
    	serializer.is_valid(raise_exception=True)
    	instance = serializer.save()

    	for x in range(i):
    		request.data[x]['transactionid'] = instance.id
    	
    	serializerDetail = TransactionDetailSerializer(data=request.data,many=True)
    	serializerDetail.is_valid(raise_exception=True)
    	serializerDetail.save()
    	returnData = serializer.data
    	returnData["items"] = serializerDetail.data
    	return Response(returnData)

    def list(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Transaction.objects.all()
        transaction = get_object_or_404(queryset, id=pk)
        serializer = TransactionSerializer(transaction)

        querysetDetail = TransactionDetail.objects.filter(transactionid=pk)
        serializerDetail = TransactionDetailSerializer(querysetDetail,many=True)
        returnData = serializer.data
        returnData["items"] = serializerDetail.data
        return Response(returnData)

    def put(self, request, pk, format=None):
        transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = Transaction.objects.get(id=pk)
        queryset.delete()
        return Response({"detail":"Delete Success id "+str(pk)})

    def partial_update(self, request, pk):
        transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
