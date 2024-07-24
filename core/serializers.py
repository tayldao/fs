from __future__ import annotations

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import PaymentDetails, Bank, Kyc, NOK
from authy.models import Country, State, City


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
        extra_kwargs = {"client": {"read_only": True}}


class KycSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Kyc
        extra_kwargs = {"client": {"read_only": True}}


class PaymentDetailsSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PaymentDetails
        extra_kwargs = {"client": {"read_only": True}}
