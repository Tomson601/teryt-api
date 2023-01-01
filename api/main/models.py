from django.db import models


class Wojewodztwo(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    woj_id = models.CharField(max_length=150, null=False, unique=True)
    status_on_day =models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name

class Powiat(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    pow_id = models.CharField(max_length=150, null=False)
    status_on_day = models.CharField(max_length=150, null=False)
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Gmina(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    status_on_day = models.CharField(max_length=150, null=False)
    gmi_id = models.CharField(max_length=150, null=False)
    powiat = models.ForeignKey(Powiat, on_delete=models.PROTECT)
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
