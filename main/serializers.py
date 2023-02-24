from rest_framework import serializers
from main import models


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseCategory
        exclude = ["created_at", ]


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="title",
        queryset=models.ExpenseCategory.objects.all(),
        required=False
    )

    class Meta:
        model = models.Expense
        exclude = ["created_at", ]
