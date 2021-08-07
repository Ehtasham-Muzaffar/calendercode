from django.contrib import admin
from events.models import Myclubuser
from events.models import Venue
from events.models import Event
# Register your models here.
admin.site.register(Myclubuser)
admin.site.register(Venue)
admin.site.register(Event)
