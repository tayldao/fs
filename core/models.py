from django.db import models

from mixins.base_model import BaseModel
from authy.models import User, Country, State


class Kyc(BaseModel):
    client = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=(("Male", "M"), ("Female", "F")),
    )
    address = models.TextField()
    id_type = models.CharField(
        choices=(
            ("NIN", "NIN"),
            ("BVN", "BVN"),
            ("Drivers License", "Drivers License"),
        ),
        max_length=16,
    )
    id_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.client.first_name} {self.client.last_name} Address"


class NOK(BaseModel):
    client = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    relationship = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=10,
        choices=(("Male", "M"), ("Female", "F")),
    )
    phone_number = models.CharField(max_length=12)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.client.first_name} {self.client.last_name} Address"


class Bank(BaseModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"


class PaymentDetails(BaseModel):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.client.first_name} {self.client.last_name} {self.bank.name} Account Details"
