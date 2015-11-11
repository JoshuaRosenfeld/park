from django.contrib import admin
from .models import Instance

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('start', 'end')

admin.site.register(Instance, InstanceAdmin)