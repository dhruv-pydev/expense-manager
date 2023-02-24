from rest_framework import serializers
from rest_framework import exceptions
from main import models


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseCategory
        exclude = ["created_on", "modified_on"]


class ExpenseSerializer(serializers.ModelSerializer):

    # def validate(self, attrs):
    #     expense_category = attrs.pop("category", None)
    #     expense_categories = self.context.get("expense_categories", [])

    #     if not expense_category:
    #         return super().validate(attrs)

    #     if expense_category in expense_categories:
    #         attrs["category"] = models.ExpenseCategory.objects.get(
    #             title=expense_category)
    #     else:
    #         data = {"title": expense_category, "user": attrs.get("user").id}
    #         serializer = ExpenseCategorySerializer(data=data)
    #         if serializer.is_valid():
    #             attrs["category"] = serializer.save()
    #             return super().validate(attrs)
    #         else:
    #             raise exceptions.ValidationError(serializer.errors)

    category = serializers.SlugRelatedField(
        slug_field="title",
        queryset=models.ExpenseCategory.objects.all(),
        required=True
    )

    class Meta:
        model = models.Expense
        exclude = ["created_on", "modified_on"]
