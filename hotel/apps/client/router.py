from rest_framework.routers import DefaultRouter
from apps.client.views import ClientViewSet

router = DefaultRouter()

router.register(r'clients',ClientViewSet,basename = 'clients')

urlpatterns = router.urls
