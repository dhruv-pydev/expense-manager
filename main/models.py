from django.db import models

from user_management import models as user_management_models


class ExpenseCategory(user_management_models.BaseModel):
    title = models.CharField(max_length=255, unique=True)

    user = models.ForeignKey(
        to=user_management_models.MainUser,
        on_delete=models.CASCADE,
        related_name="user_expense_categories",
        # null=True,
        # blank=True
    )

    def __str__(self) -> str:
        return self.title if self.title else "-"

    class Meta:
        verbose_name_plural = "Expense Categories"


class Expense(user_management_models.BaseModel):
    user = models.ForeignKey(
        to=user_management_models.MainUser,
        on_delete=models.CASCADE,
        related_name="user_expenses"
    )

    description = models.CharField(max_length=255, null=True, blank=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        to=ExpenseCategory,
        related_name="category_expenses",
        on_delete=models.CASCADE,
        # null=True,
        # blank=True
    )

    def __str__(self) -> str:
        description = f"{self.description[:10]}..." if self.description else "-"
        return f"{self.amount}: {self.category.__str__()}: {description}"
