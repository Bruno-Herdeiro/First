from django.contrib import admin
from .models import Ticket, ProcessCalendar

# Register your models here.

admin.site.register(Ticket)
admin.site.register(ProcessCalendar)
