from django.db import models


# Create your models here.
class Cv(models.Model):
    foto = models.CharField(max_length=100)
    desiredEmploy = models.CharField(max_length=50)
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    position = models.OneToOneField('Position', on_delete=models.CASCADE)


class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=50)
    cp = models.CharField(max_length=8)
    local = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Email(models.Model):
    email = models.EmailField()
    type = models.CharField(max_length=50)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)


class Contact(models.Model):
    countryPrefix = models.CharField(max_length=3)
    phone = models.CharField(max_length=9)
    fax = models.CharField(max_length=9)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Position(models.Model):
    startMonth = models.CharField(max_length=9)
    startYear = models.CharField(max_length=4)
    endMonth = models.CharField(max_length=9)
    endYear = models.CharField(max_length=4)
    occupation = models.CharField(max_length=50)
    businessSector = models.CharField(max_length=50)
    employer = models.OneToOneField('Employer', on_delete=models.CASCADE)


class Activity(models.Model):
    designation = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Employer(models.Model):
    name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    www = models.CharField(max_length=50)
    email = models.EmailField()
