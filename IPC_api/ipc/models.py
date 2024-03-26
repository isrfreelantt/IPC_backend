from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.brand} {self.model}"

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
    campaign = models.IntegerField()

    def __str__(self):
        return f"{self.coverage_type} {self.name} {self.value} {self.campaign}"

class Premium(models.Model):
    sum_insured = models.CharField(max_length=25)
    premium = models.IntegerField()
    campaign = models.IntegerField()
    age = models.CharField(max_length=5)
    deduct = models.CharField(max_length=100)
    garage = models.CharField(max_length=10)
    cars = models.ManyToManyField('Car', through='Premium_Car', related_name='premium')



    def __str__(self):
        return f"{self.sum_insured} {self.premium} {self.campaign} {self.age} {self.deduct} {self.garage}"

class Premium_Car(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='id')
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return f"{self.model} {self.premium}"
