from __future__ import annotations

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import PaymentDetails, Country, State, Bank, Kyc, NOK


class StateSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = State


class CountrySerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Country


class BankSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Bank


class NOKSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = NOK


class KycSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Kyc


class PaymentDetailsSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PaymentDetails
