from django.contrib import admin
from .models import Menu, Booking, Take, Category, Contact

# Register your models here.
admin.site.register(Booking)
admin.site.register(Take)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Contact)