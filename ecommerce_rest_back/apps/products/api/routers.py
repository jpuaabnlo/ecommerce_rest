from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename = 'products')
router.register(r'measure-unit', MeasureUnitListAPIView, basename='measure_unit')
router.register(r'indicator', IndicatorListAPIView, basename='indicator')
router.register(r'category-product', CategoryProductListAPIView, basename = 'category_product')

urlpatterns = router.urls