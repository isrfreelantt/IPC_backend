from django.db import models
from phone_field import PhoneField

class Brand(models.Model):
    brand_code = models.CharField(4)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand_code} {self.brand}"

class Car(models.Model):
    brand_code = models.CharField(4)
    model_code = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    min_year = models.IntegerField(null=True)
    max_year = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.brand_code} {self.model_code} {self.model} {self.min_year} {self.max_year}"

class Spec(models.Model):
    vehicle_key = models.CharField(max_length=10)
    model_code = models.CharField(max_length=30)
    model_spec = models.CharField(max_length=100)
    year = models.IntegerField()
    body_type = models.CharField(max_length=20)
    min_sum_insured = models.IntegerField()
    max_sum_insured = models.IntegerField()

    def __str__(self):
        return f"{self.vehiclekey} {self.model_code} {self.model_spec} {self.body_type} {self.year} {self.min_sum_insured} {self.max_sum_insured}"

class Package(models.Model):
    package_type = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.package_type} {self.name} {self.company}"

class Coverage(models.Model):
    coverage_type = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=20)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, to_field='id', related_name='coverages')

    def __str__(self):
        return f"{self.coverage_type} {self.name} {self.value} {self.package}"

class Premium(models.Model):
    min_sum_insured = models.IntegerField(null=True)
    max_sum_insured = models.IntegerField(null=True)
    premium = models.IntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, to_field='id', related_name='premiums')
    min_age = models.SmallIntegerField(null=True)
    max_age = models.SmallIntegerField(null=True)
    deduct = models.CharField(max_length=100)
    garage = models.CharField(max_length=10)
    cars = models.ManyToManyField('Car', through='Premium_Car', related_name='premium')
    location = models.CharField(max_length=30)
    cctv = models.FloatField()

    def __str__(self):
        return f"{self.min_sum_insured} {self.max_sum_insured} {self.premium} {self.package} {self.min_age} {self.max_age} {self.deduct} {self.garage} {self.location} {self.cctv}"


class Premium_Car(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='id')
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return f"{self.model} {self.premium}"
    
class Province(models.Model):
    province_th = models.CharField(max_length=30)
    province_en = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.province_th} {self.province_en}"

class Car_Owned(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, to_field='id')
    model = models.CharField(max_length=30)
    submodel = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, to_field='id')
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
