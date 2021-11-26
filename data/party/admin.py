from django.contrib import admin

# Register your models here.

from party.models import *

admin.site.register(Party)
admin.site.register(LocalsParty)
admin.site.register(Tickets)