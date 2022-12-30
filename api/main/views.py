from main import models, serializers
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render


# Create your views here.
class WojewodztwoViewSet(ModelViewSet):
    queryset = models.Wojewodztwo.objects.all()
    serializer_class = serializers.WojewodztwoSerializer
    lookup_field = "woj_id"
    lookup_url_kwarg = "woj_id"
    http_method_names = ["get"]
