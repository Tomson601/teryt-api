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

class PowiatViewSet(ModelViewSet):
    queryset = models.Powiat.objects.all()
    serializer_class = serializers.PowiatSerializer
    lookup_field = "pow_id"
    lookup_url_kwarg = "pow_id"
    http_method_names = ["get"]

class GminaViewSet(ModelViewSet):
    queryset = models.Gmina.objects.all()
    serializer_class = serializers.GminaSerializer
    lookup_field = "gmi_id"
    lookup_url_kwarg = "gmi_id"
    http_method_names = ["get"]

class MiejscowoscViewSet(ModelViewSet):
    queryset = models.Miejscowosc.objects.all()
    serializer_class = serializers.MiejscowoscSerializer
    lookup_field = "miejsc_id"
    lookup_url_kwarg = "miejsc_id"
    http_method_names = ["get"]
