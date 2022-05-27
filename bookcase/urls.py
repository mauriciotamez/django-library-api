from .views import BookItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("book-catalog", BookItemViewSet)
urlpatterns = router.urls