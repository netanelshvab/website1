from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phoneNumber = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    photo = models.IntegerField(null=True)
    price = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.price}"