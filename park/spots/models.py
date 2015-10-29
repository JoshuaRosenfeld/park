from django.db import models

class User(models.Model):
	name = models.CharField(max_length=70)
	nickname = models.CharField(max_length=70)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

class Residence(models.Model):
	address = models.CharField(max_length=500)
	user = models.ForeignKey(User)

class Spot(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=140)
	residence = models.ForeignKey(Residence)

class Instance(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	rate = models.DecimalField(max_digits=8, decimal_places=2)
	spot = models.ForeignKey(Spot)

class Transaction(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeFiled()
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	guest = models.ForeignKey(User)
	instance = models.ForeignKey(Instance)