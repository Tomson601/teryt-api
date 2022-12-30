from django.urls import include, path
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'wojewodztwa', views.WojewodztwoViewSet)
router.register(r'powiaty', views.PowiatViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
