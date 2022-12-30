from django.urls import include, path
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'wojewodztwa', views.WojewodztwoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
