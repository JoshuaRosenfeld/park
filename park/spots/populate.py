from django.contrib.auth.models import User
from .models import Residence, Spot, Instance
from . import helper
import random, datetime, pytz
from datetime import date

def main(users, residences, spots, instances):
	if users: populateUsers()
	if residences: populateResidences()
	if spots: populateSpots()
	if instances: populateInstances()

def populateUsers():
	email = 'jlr0802@gmail.com'
	first_name = 'Josh'

	for i in range(0, 100):
		username = 'username%d' % (i)
		password = 'password%d' % (i)
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.save()
		#print(user)

def populateResidences():
	addresses = [
		'300 York St #1, New Haven, CT 06511',
		'120 High St, New Haven, CT 06511',
		'68 High St, New Haven, CT 06511',
		'1080 Chapel St, New Haven, CT 06510',
		'1156 Chapel St, New Haven, CT 06511',
		'247 College St, New Haven, CT 06510',
		'220 College St, New Haven, CT 06510',
		'196 Crown St, New Haven, CT 06510',
		'116 Crown St, New Haven, CT 06510',
		'20 Church St, New Haven, CT 06510',
		'175 Water St, New Haven, CT 06511',
		'1 Park St, New Haven, CT 06510',
		'140 Legion Ave, New Haven, CT 06519',
		'2 Boston Post Rd, West Haven, CT 06516',
		'73 Sachem St, New Haven, CT 06511',
		'170 Whitney Ave, New Haven, CT 06511',
		'114 Whitney Ave, New Haven, CT 06510',
		'874 State St, New Haven, CT 06511',
		'2 Mechanic St, New Haven, CT 06511',
		'409 Prospect St, New Haven, CT 06511',
		'342 Winchester Ave, New Haven, CT 06511',
		'379 Whalley Ave, New Haven, CT 06511',
		'259 Edgewood Ave, New Haven, CT 06511',
		'101 Hubinger St, New Haven, CT 06511',
		'986 Forest Rd, New Haven, CT 06515',
		'896 Whalley Ave, New Haven, CT 06515',
	]

	for address in addresses:
		user = User.objects.order_by('?').first()
		lat, lng = helper.getLatLng(address)
		residence = Residence(address=address, user=user, lat=lat, lng=lng)
		residence.save()
		#print(residence)

def populateSpots():
	names = [
		'Driveway',
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
		'Big enough for minivans.',
		'Please leave room on left.',
		'Please back in.',
		'The spot only fits sedans.',
		'Park near the basketball hoop',
		'Park in front of the street lamp',
		'Park near the mailbox',
	]

	num = Residence.objects.all().count() - 1
	residences = Residence.objects.order_by('id')
	for i in range(0, num):
		name = random.sample(names, 1)[0]
		desc = random.sample(descriptions, 1)[0]
		residence = residences[i]
		spot = Spot(name=name, description=desc, residence=residence)
		spot.save()
		#print(spot)

def populateInstances():
	booked = False

	today_date = date.today()
	midnight = datetime.datetime.strptime("12:00 AM", "%I:%M %p").time()
	today = datetime.datetime.combine(today_date, midnight)
	today = pytz.utc.localize(today)

	num = Spot.objects.all().count() - 1
	spots = Spot.objects.order_by('id')
	for i in range(0, num):
		spot = spots[i]
		for i in range(0, 365):
			x = random.randint(1, 3) # only assign instances 2/3 of the time
			if x < 3:
				rate = random.randrange(1, 10, 1)
				hours = random.randrange(0, 25, 1)
				minutes = random.randrange(0, 60, 15)
				start_offset = datetime.timedelta(days=i, hours=hours, minutes=minutes)
				start = today + start_offset

				length = random.randrange(15, 1440, 15)
				end_offset = datetime.timedelta(minutes=length)
				end = start + end_offset

				instance = Instance(start=start, end=end, rate=rate, booked=booked, spot=spot)
				instance.save()
				#print(instance)
