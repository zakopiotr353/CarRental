from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)
class Car(models.Model):
    ENGINE_TYPES = [
        ("benzynowy", "Benzynowy"),
        ("diesel", "Diesel"),
        ("hybrydowy", "Hybrydowy"),
        ("elektryczny", "Elektryczny"),
        ("wodorowy", "Wodorowy")
    ]
    GEARBOX_TYPES = [
        ("automatyczna", "Automatyczna"),
        ("manualna", "Manualna"),
        ("polautomatyczna", "Polautomatyczna"),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    seats_count = models.PositiveSmallIntegerField() 
    dors_count = models.PositiveSmallIntegerField()
    fuel_usage = models.FloatField()
    engine_power = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    equipment = models.ManyToManyField(Equipment)
    gearbox_type = models.CharField(max_length=20, choices=GEARBOX_TYPES)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.DecimalField(max_digits=10, decimal_places=2)


class Address(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=10)
    appartment_no = models.CharField(max_length=10)

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", "dowód osobisty"),
        ("paszport", "paszport"),
        ("prawo_jazdy", "prawo jazdy")
    ]
    phone = models.CharField(max_length=20)
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES)
    identity_document_no = models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT)

class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotowka"),
        ("przelew", "Przelew"),
        ("blik", "Blik"),
    ]
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    declared_order_duration = models.DurationField()
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField()

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        # fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id']
        # fields = ['country', 'city', 'post_code', 'street', 'building_no', 'appartment_no']