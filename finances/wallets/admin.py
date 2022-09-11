from django.contrib import admin

from .models import Category, Transaction


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "created_at")
    list_filter = ("created_at",)
    fields = ("title",)


class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner")
    list_display = ("owner", "title", "amount", "transaction_type", "category")
    list_filter = ("transaction_type", "created_at")
    fields = ("owner", "title", "amount", "transaction_type", "category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
