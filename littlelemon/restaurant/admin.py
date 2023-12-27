from django.contrib import admin

# Register your models here.
from .models import Booking, Table

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    date_hierarchy = 'booking_date'

class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    search_fields = ('title',)

# Register models with the custom admin classes
admin.site.register(Booking, BookingAdmin)
admin.site.register(Table, TableAdmin)