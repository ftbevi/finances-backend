from rest_framework import serializers

from .models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)


class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = ("title", "transaction_type", "category", "amount", "owner")
