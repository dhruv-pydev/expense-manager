from rest_framework import routers

from main import views

from user_management import urls as user_management_urls

router = routers.DefaultRouter()

router.register(
    prefix="expense_category",
    viewset=views.ExpenseCategoryViewSet,
    basename="expense_category"
)

router.register(
    prefix="expense",
    viewset=views.ExpenseViewSet,
    basename="expense"
)

router.registry.extend(user_management_urls.user_management_router.registry)

urlpatterns = router.urls
