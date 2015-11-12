from django.contrib import admin
from .models import Residence, Spot, Instance, Transaction

class ResidenceAdmin(admin.ModelAdmin):
	list_display = ('address', 'lat', 'lng', 'user')

class SpotAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'residence')

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('start', 'end', 'rate', 'booked')

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('start', 'end', 'cost', 'guest', 'instance')

admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Instance, InstanceAdmin)
admin.site.register(Transaction, TransactionAdmin)