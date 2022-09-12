from django.urls import path
from rest_framework import routers

from .views import BalanceViewSet, TransactionViewSet

wallet_router = routers.DefaultRouter()
wallet_router.register(r"", TransactionViewSet)

urlpatterns = [
    path(r"balance", BalanceViewSet.as_view()),
]
urlpatterns += wallet_router.urls
