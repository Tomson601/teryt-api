from django.urls import include, path
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'wojewodztwa', views.WojewodztwoViewSet)
router.register(r'powiaty', views.PowiatViewSet)
router.register(r'gminy', views.GminaViewSet)
router.register(r'miejscowosci', views.MiejscowoscViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
