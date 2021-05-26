from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerProfileViewSet,
    InviteCodeViewSet,
    CustomerProfileViewSet,
    NotificationViewSet,
)

router = DefaultRouter()
router.register("notification", NotificationViewSet)
router.register("invitecode", InviteCodeViewSet)
router.register("customerprofile", CustomerProfileViewSet)
router.register("taskerprofile", TaskerProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
