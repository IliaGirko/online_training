from rest_framework.routers import DefaultRouter

from . import views
from .apps import UsersConfig

router = DefaultRouter()

router.register("users", views.UserViewSet, basename="users")

app_name = UsersConfig.name

urlpatterns = [] + router.urls
