
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer


class CouponApply(APIView):
    """
    Chec a cupon for existance
    """
    def post(self, request):
      now = timezone.now()
      code = request.data['code']
      print(code)
      try:
        coupon = Coupon.objects.get(
  				code__iexact=code,
  				valid_from__lte=now,
  				valid_to__gte=now,
  				active=True
  				)
        res = CouponSerializer(coupon).data
      except Coupon.DoesNotExist:
        coupon = None
        res = False
      return Response(res)

