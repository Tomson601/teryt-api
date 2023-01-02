from django.db import models


class Wojewodztwo(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    woj_id = models.CharField(max_length=150, null=False, unique=True)
    status_on_day =models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "extra_name": self.extra_name,
            "woj_id": self.woj_id
        }


class Powiat(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    pow_id = models.CharField(max_length=150, null=False)
    status_on_day = models.CharField(max_length=150, null=False)
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "extra_name": self.extra_name,
            "pow_id": self.pow_id,
            "wojewodztwo": {
                "name": self.wojewodztwo.name,
                "woj_id": self.wojewodztwo.woj_id,
                "id": self.wojewodztwo.id,
            },
        }

class Gmina(models.Model):
    name = models.CharField(max_length=150, null=False)
    extra_name = models.CharField(max_length=150, null=False)
    gmi_id = models.CharField(max_length=150, null=False)
    status_on_day = models.CharField(max_length=150, null=False)
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.PROTECT)
    powiat = models.ForeignKey(Powiat, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "extra_name": self.extra_name,
            "gmi_id": self.gmi_id,
            "wojewodztwo": {
                "name": self.wojewodztwo.name,
                "woj_id": self.wojewodztwo.woj_id,
                "id": self.wojewodztwo.id,
            },
            "powiat": {
                "name": self.powiat.name,
                "pow_id": self.powiat.pow_id,
                "id": self.powiat.id,
            },
        }

class Miejscowosc(models.Model):
    name = models.CharField(max_length=150, null=False)
    miejsc_id = models.CharField(max_length=150, null=False)
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.PROTECT)
    powiat = models.ForeignKey(Powiat, on_delete=models.PROTECT)
    gmina = models.ForeignKey(Gmina, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "miejsc_id": self.miejsc_id,
            "wojewodztwo": {
                "name": self.wojewodztwo.name,
                "woj_id": self.wojewodztwo.woj_id,
                "id": self.wojewodztwo.id,
            },
            "powiat": {
                "name": self.powiat.name,
                "pow_id": self.powiat.pow_id,
                "id": self.powiat.id,
            },
            "gmina": {
                "name": self.gmina.name,
                "gmi_id": self.gmina.gmi_id,
                "id": self.gmina.id,
            },
        }
