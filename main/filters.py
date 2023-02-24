from django_filters import rest_framework
from main import models
from django.db.models import Q


class ExpenseCategoryFilter(rest_framework.FilterSet):
    user = rest_framework.CharFilter(method="get_user")

    def get_user(self, queryset, name, value):
        values = value.split(",")
        qs1 = Q(user__id__in=values)
        qs2 = Q(user__user__username__in=values)
        return queryset.filter(qs1 | qs2)

    class Meta:
        model = models.ExpenseCategory
        fields = ["user"]


class ExpenseFilter(rest_framework.FilterSet):
    category = rest_framework.CharFilter(method="category_title")
    user = rest_framework.CharFilter(method="get_user")

    start_date = rest_framework.DateFilter(
        field_name="created_on",
        lookup_expr="gte"
    )

    end_date = rest_framework.DateFilter(
        field_name="created_on",
        lookup_expr="lte"
    )

    def get_user(self, queryset, name, value):
        values = value.split(",")
        qs1 = Q(user__id__in=values)
        qs2 = Q(user__user__username__in=values)
        return queryset.filter(qs1 | qs2)

    def category_title(self, queryset, name, value):
        category_title_list = value.split(",")
        return queryset.filter(category__title__in=category_title_list)

    class Meta:
        model = models.Expense
        fields = ["category", "user", "start_date", "end_date"]
