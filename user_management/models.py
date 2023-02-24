import uuid

from django.db import models
from django.contrib.auth import models as auth_models


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MainUser(BaseModel):
    user = models.OneToOneField(
        to=auth_models.User,
        related_name="main_user",
        on_delete=models.CASCADE
    )

    contact_number = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Main User"
        ordering = ("-created_on",)

    def __str__(self) -> str:
        return f"{self.user.username}"

    @property
    def full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def username(self) -> str:
        return f"{self.user.username}"

    @property
    def first_name(self) -> str:
        return f'{self.user.first_name}'

    @property
    def last_name(self) -> str:
        return f'{self.user.last_name}'

    @property
    def email(self) -> str:
        return f'{self.user.email}'
