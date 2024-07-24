from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from core.views import *


router = SimpleRouter()
router.register(r"kyc", KycViewset, basename="kyc")
router.register(r"nok", NOKViewset, basename="nok")
router.register(r"payment-details", PaymentDetailsViewset, basename="payment_details")
router.register(r"states", StateViewset, basename="states")
router.register(r"countries", CountryView, basename="countries")
router.register(r"banks", BankViewset, basename="banks")
urlpatterns = []
urlpatterns += router.urls
