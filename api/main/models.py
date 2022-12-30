from django.db import models


class Wojewodztwo(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    woj_id = models.CharField(max_length=150, null=False, unique=True)
    status_on_day =models.CharField(max_length=150, null=False)

    def __str__(self):
        return {
            self.name,
            self.woj_id
        }
