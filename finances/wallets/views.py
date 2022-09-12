from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import TransactionFilter
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


class BalanceViewSet(APIView):
    def get(self, request):
        data = Transaction.balance(user=request.user)
        return Response(data)
