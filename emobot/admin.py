from django.contrib import admin

from emobot.models import Admin, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Admin)

