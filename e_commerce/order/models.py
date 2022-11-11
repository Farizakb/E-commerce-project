from django.db import models
from blog.models import AbstractModel
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Country(AbstractModel):
    countries = models.CharField(verbose_name="Country", max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.countries

    


class City(AbstractModel):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country", related_name="City_Country")
    cities = models.CharField(verbose_name="City",max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.cities



class ShippingAddress(AbstractModel):
    user = models.ForeignKey(User, related_name="shipping_address", on_delete=models.CASCADE,)
    company_name = models.CharField(verbose_name="Company name", max_length=255,  null=True, blank=True)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="Shipping_Country")
    cities = models.ForeignKey(City, on_delete=models.CASCADE, related_name="Shipping_City")
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.user.username} -- > {self.address}'