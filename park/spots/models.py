from django.db import models

class User(models.Model):
	name = models.CharField(max_length=70)
	nickname = models.CharField(max_length=70)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Residence(models.Model):
	address = models.CharField(max_length=500)
	user = models.ForeignKey(User)

	def __str__(self):
		return "%s lives at %s" % (self.user.name, self.address)

class Spot(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=140)
	residence = models.ForeignKey(Residence)

	def __str__(self):
		return "%s at %s" % (self.name, self.residence.address)

class Instance(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	rate = models.DecimalField(max_digits=8, decimal_places=2)
	spot = models.ForeignKey(Spot)

	def __str__(self):
		start_str = self.start.strftime("%c")
		end_str = self.end.strftime("%c")
		return "Spot %d available from %s to %s" % (self.spot.id, start_str, end_str)

class Transaction(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	guest = models.ForeignKey(User)
	instance = models.ForeignKey(Instance)

	def __str__(self):
		return "%s paid %d for spot %d" % (self.guest.name, self.cost, self.instance.spot.id)