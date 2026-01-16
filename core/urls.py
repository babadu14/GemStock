from core.views import StockListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stocks', StockListViewSet, basename='stock')

urlpatterns = router.urls
