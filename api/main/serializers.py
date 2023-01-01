from rest_framework import serializers
from main import models


class WojewodztwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wojewodztwo
        fields = ["id", "name", "extra_name", "woj_id", "status_on_day"]

class PowiatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Powiat
        fields = ["id", "name", "extra_name", "pow_id", "status_on_day", "wojewodztwo"]

class GminaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gmina
        fields = ["id", "name", "extra_name", "gmi_id", "status_on_day", "wojewodztwo", "powiat"]

class MiejscowoscSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Miejscowosc
        fields = ["id", "name", "extra_name", "miejsc_id", "status_on_day", "wojewodztwo", "powiat", "gmina"]
