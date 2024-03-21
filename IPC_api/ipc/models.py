from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Car_detail(models.Model):
    model = models.IntegerField
    submodel = models.CharField(max_length=30)
    year = models.IntegerField
    MIN_SUM_INSURED = models.IntegerField
    MAX_SUM_INSURED = models.IntegerField

    def __str__(self):
        return f"{self.model} {self.submodel} {self.year} {self.MIN_SUM_INSURED} {self.MAX_SUM_INSURED}"

class Campaign(models.Model):
    insurance_type = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.insurance_type} {self.name} {self.company}"
    
class Coverage(models.Model):
    coverage_type = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=20)
    campaign = models.IntegerField

    def __str__(self):
        return f"{self.coverage_type} {self.name} {self.value} {self.campaign}"

class Premiums(models.Model):
    sum_insured = models.CharField(max_length=25)
    premium = models.IntegerField
    campaign_id = models.IntegerField
    age = models.CharField(max_length=5)
    deduct = models.CharField(max_length=100)
    garage = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.sum_insured} {self.premium} {self.campaign_id} {self.age} {self.deduct} {self.garage}"



