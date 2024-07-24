from django.db.transaction import atomic
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from core.serializers import *
from core.models import PaymentDetails, Bank, Kyc, NOK
from authy.models import Country, State


class PaymentDetailsViewset(ModelViewSet):
    serializer_class = PaymentDetailsSerializer
    queryset = PaymentDetails.objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class CountryView(ModelViewSet):
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    queryset = Country.objects.all()
    http_method_names = ["get"]


class StateViewset(ModelViewSet):
    serializer_class = StateSerializer
    permission_classes = (AllowAny,)
    queryset = State.objects.all()
    http_method_names = ["get"]


class BankViewset(ModelViewSet):
    serializer_class = BankSerializer
    permission_classes = (AllowAny,)
    queryset = Bank.objects.all()
    http_method_names = ["get"]


class NOKViewset(ModelViewSet):
    serializer_class = NOKSerializer
    queryset = NOK.objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class KycViewset(ModelViewSet):
    serializer_class = KycSerializer
    queryset = Kyc.objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
