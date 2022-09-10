from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)
    deleted_at = models.DateTimeField(
        verbose_name="Deletado às", blank=True, null=True, default=None
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class User(AbstractUser, BaseModel):
    full_name = models.CharField(verbose_name="Nome", max_length=255, blank=True)
    phone = models.CharField(
        verbose_name="Telefone", max_length=12, null=True, blank=True
    )
    email = models.EmailField(verbose_name="Email", blank=True, unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
