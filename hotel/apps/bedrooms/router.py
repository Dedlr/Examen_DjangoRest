from rest_framework.routers import DefaultRouter
from apps.bedrooms.views import BedroomViewSet

router = DefaultRouter()

router.register(r'bedrooms',BedroomViewSet,basename = 'bedrooms')

urlpatterns = router.urls
