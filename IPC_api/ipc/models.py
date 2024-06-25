from django.db import models
from phone_field import PhoneField

class Brand(models.Model):
    brandcode = models.CharField(4)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brandcode} {self.brand}"

class Car(models.Model):
    brandcode = models.CharField(4)
    modelcode = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    min_year = models.IntegerField(null=True)
    max_year = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.brandcode} {self.modelcode} {self.model} {self.min_year} {self.max_year}"

class Car_detail(models.Model):
    model = models.IntegerField()
    sub_model = models.CharField(max_length=30)
    year = models.IntegerField()
    min_sum_insured = models.IntegerField()
    max_sum_insured = models.IntegerField()

    def __str__(self):
        return f"{self.model} {self.sub_model} {self.year} {self.min_sum_insured} {self.max_sum_insured}"

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
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='id', related_name='coverages')

    def __str__(self):
        return f"{self.coverage_type} {self.name} {self.value} {self.campaign}"

class Premium(models.Model):
    min_sum_insured = models.IntegerField(null=True)
    max_sum_insured = models.IntegerField(null=True)
    premium = models.IntegerField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='id')
    min_age = models.SmallIntegerField(null=True)
    max_age = models.SmallIntegerField(null=True)
    deduct = models.CharField(max_length=100)
    garage = models.CharField(max_length=10)
    cars = models.ManyToManyField('Car', through='Premium_Car', related_name='premium')

    def __str__(self):
        return f"{self.min_sum_insured} {self.max_sum_insured} {self.premium} {self.campaign} {self.min_age} {self.max_age} {self.deduct} {self.garage}"

class Premium_Car(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='id')
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return f"{self.model} {self.premium}"
    
class Province(models.Model):
    province = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.province}"

class Car_Owned(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    submodel = models.CharField(max_length=30)
    province = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.submodel} {self.province} {self.year}"
    
class Customer(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    tel = PhoneField()
    email = models.EmailField()
    car_owned = models.ForeignKey(Car_Owned, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return f"{self.name} {self.surname} {self.tel} {self.email} {self.car_owned}"