from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product, Document
import stripe
from django.http import JsonResponse



class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(user=self.request.user)

class OrderViewSet(OwnerMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)



class OrderAndPay(APIView):
    """
    Create an Order and try to charge
    """
    def post(self, request):
        comprados = []
        mensaje = 'nada'
        # permission_classes = (permissions.IsAuthenticated,)
        data = request.data
        print(data)
        order = Order.objects.create(user=request.user)
        print('la orden:', order)
        for i in data['items']:
            product = Product.objects.get(id=i['product'])
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=product.price,
                                     quantity=i['quantity'])
            comprados.append(product)
        total = order.get_total_cost()
        print('el total',total)

        #stripe
        stripe.api_key = 'sk_test_zWlHDjttH9ag2aLf4cxF9QhE'
        try:
            mensaje = 'paso el try'
            stripe.Charge.create(
                amount=int(total*100),
                currency="cad",
                description="Cargo por recurso Erick de la Parra",
                source=data['token'],  # obtained with Stripe.js
            )
            order.paid = True
            order.save()
            for c in comprados:
                try:
                    d = c.documents.all()[0]
                    d.users.add(request.user)
                except:
                    pass
                

        except Exception as e:
            print(e)
            mensaje = "Ocurrió un error"
            # mensaje = e


        return JsonResponse(mensaje, safe=False)


#class ItemsCreateView(generics.CreateAPIView):
    """Permite recibir una lista de objetos y crearlos uno por uno"""
 #   queryset = OrderItem.objects.all()
  #  serializer_class = OrderItemSerializer

#    def get_serializer(self, instance=None, data=None, many=False, partial=False):
 #       return super(ItemsCreateView, self).get_serializer(instance=instance, data=data, many=True, partial=partial)
