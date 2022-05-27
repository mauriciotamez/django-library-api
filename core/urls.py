from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users",UserViewSet)
urlpatterns = router.urls