from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Payments, User
from .serializers import PaymentsModelSerializer, UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsModelSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("date_payments",)
    filterset_fields = ("paid_lesson", "paid_course", "payment_method")
