from rest_framework import routers

from .views import TransactionViewSet

wallet_router = routers.DefaultRouter()
wallet_router.register(r"", TransactionViewSet)

# urlpatterns = [
#     path(r'investiments/<int:investiment_id>/balance', BalanceViewSet.as_view()),
#     path(r'investiments/withdrawal', WithdrawalViewSet.as_view())
# ]
urlpatterns = wallet_router.urls
