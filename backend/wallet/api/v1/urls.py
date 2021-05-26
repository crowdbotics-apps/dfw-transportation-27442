from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    TaskerPaymentAccountViewSet,
    TaskerWalletViewSet,
    PaymentMethodViewSet,
    CustomerWalletViewSet,
)

router = DefaultRouter()
router.register("customerwallet", CustomerWalletViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("taskerwallet", TaskerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
