from django.contrib.auth.models import User
from .models import Residence, Spot, Instance
import random, datetime
from datetime import date

def populateUsers():
	email = 'jlr0802@gmail.com'
	first_name = 'Josh'

	for i in range(0, 100):
		username = 'user%d' % (i)
		password = 'password%d' % (i)
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.save()

def populateResidences():
	addresses = [
	]

	for address in addresses:
		user = User.objects.order_by('?').first()
		residence = Residence(address=address, user=user)
		residence.save()

def populateSpots():
	names = [
		'Driveway',
		'Left side of driveway',
		'Street',
		'Back lot',
		'Spot #1',
		'Spot #2',
		'Spot #3',
		'Spot A',
		'Spot B',
		'Spot C',
	]

	descriptions = [
		'Please leave on time.',
		'Room for minivans.',
		'Please leave room for other cars.',
		'Please back in.',
		'The spot only fits sedans.',
		'Park near the basketball hoop',
		'Park in front of the street lamp',
		'Park near the mailbox',
	]

	for i in range(0, Residence.objects.all().count() - 1):
		name = random.sample(names, 1)[0]
		desc = random.sample(descriptions, 1)[0]
		residence = Residence.objects.order_by('id')[i]
		spot = Spot(name=name, description=desc, residence=residence)
		spot.save()

def populateInstances():
	booked = False
	rate = random.randrange(0.25, 10, 0.5)

	today = date.today()
	for i in range(0, Spots.objects.all().count() - 1):
		spot = Spot.objects.order_by('id')[i]
		for i in range(0, 365):
			x = random.randint(1, 3)
			if x < 3:
				hours = random.randrange(0, 23, 1)
				minutes = random.randrange(0, 45, 15)
				start = today + datetime.timedelta(days=i, hours=hours, minutes=minutes)

				length = random.randrange(15, 1440, 15)
				end = start + datetime.timedelta(minutes=length)

				instance = Instance(start=start, end=end, rate=rate, booked=booked, spot=spot)
				instance.save()
