from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product
import stripe
from django.http import JsonResponse



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #permission_classes = (permissions.IsAuthenticated)


class OrderAndPay(APIView):
    """
    Create an Order and try to charge
    """
    def post(self, request):
        mensaje = 'nada'
        permission_classes = (permissions.IsAuthenticated,)
        data = request.data
        order = Order.objects.create(user=request.user)
        print(order)
        for i in data['items']:
            product = Product.objects.get(id=i['product'])
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=product.price,
                                     quantity=i['quantity'])
        total = order.get_total_cost()
        print('el total',total)

        #stripe
        stripe.api_key = 'sk_test_zWlHDjttH9ag2aLf4cxF9QhE'
        try:
             mensaje = stripe.Charge.create(
                amount=total,
                currency="mxn",
                description="Cargo pro recurso Erick de la Parra",
                source="tok_visa",  # obtained with Stripe.js
            )
        except Exception as e:
            mensaje = e


        return JsonResponse(mensaje, safe=False)


#class ItemsCreateView(generics.CreateAPIView):
    """Permite recibir una lista de objetos y crearlos uno por uno"""
 #   queryset = OrderItem.objects.all()
  #  serializer_class = OrderItemSerializer

#    def get_serializer(self, instance=None, data=None, many=False, partial=False):
 #       return super(ItemsCreateView, self).get_serializer(instance=instance, data=data, many=True, partial=partial)