from rest_framework import serializers
from main import models


class WojewodztwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wojewodztwo
        fields = ["id", "name", "extra_name", "woj_id", "status_on_day"]

    def to_representation(self, instance):
        return instance.json()

class PowiatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Powiat
        fields = ["id", "name", "extra_name", "pow_id", "status_on_day", "wojewodztwo"]

    def to_representation(self, instance):
        return instance.json()


class GminaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gmina
        fields = ["id", "name", "extra_name", "gmi_id", "status_on_day", "wojewodztwo", "powiat"]

    def to_representation(self, instance):
        return instance.json()


class MiejscowoscSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Miejscowosc
        fields = ["id", "name", "miejsc_id", "wojewodztwo", "powiat", "gmina"]

    def to_representation(self, instance):
        return instance.json()

class UlicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ulica
        fields = ["id", "ul_id", "name", "second_name", "full_name", "type", "wojewodztwo", "powiat", "gmina", "miejscowosc"]

    def to_representation(self, instance):
        return instance.json()
