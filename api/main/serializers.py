from rest_framework import serializers
from main import models


class WojewodztwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wojewodztwo
        fields = ["id", "name", "extra_name", "woj_id", "status_on_day"]
