from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PaymentsViewSet, UserTokenObtainPairView, UserTokenRefreshView
from .apps import UsersConfig

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("payments", PaymentsViewSet, basename="payments")

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
