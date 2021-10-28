from django.contrib import admin

from emobot.models import Admin, User

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)

