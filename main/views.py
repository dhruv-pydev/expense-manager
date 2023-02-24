from rest_framework import viewsets
from django_filters import rest_framework

from main import models
from main import serializers
from main import filters


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ExpenseCategory.objects.all()
    serializer_class = serializers.ExpenseCategorySerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = filters.ExpenseCategoryFilter


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = filters.ExpenseFilter
