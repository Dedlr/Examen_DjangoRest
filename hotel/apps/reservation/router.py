from rest_framework.routers import DefaultRouter
from apps.reservation.views import ReservationViewSet

router = DefaultRouter()

router.register(r'reservations',ReservationViewSet,basename = 'reservations')

urlpatterns = router.urls