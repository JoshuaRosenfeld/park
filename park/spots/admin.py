from django.contrib import admin
from .models import Instance, Transaction

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('start', 'end', 'rate', 'booked')

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('start', 'end', 'cost', 'guest', 'instance')

admin.site.register(Instance, InstanceAdmin)
admin.site.register(Transaction, TransactionAdmin)