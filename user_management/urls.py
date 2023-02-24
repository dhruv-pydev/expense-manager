from rest_framework import routers
from user_management import views

user_management_router = routers.DefaultRouter()

user_management_router.register(
    prefix="user",
    viewset=views.MainUserViewSet,
    basename="user"
)

urlpatterns = user_management_router.urls
