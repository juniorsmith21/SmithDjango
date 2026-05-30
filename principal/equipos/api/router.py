from rest_framework.routers import DefaultRouter
from equipos.api.views import EquipoViewSet

router_equipos = DefaultRouter()
router_equipos.register(
    prefix='equipos',
    viewset=EquipoViewSet,
    basename='equipos'
)

urlpatterns = router_equipos.urls