from django.contrib import admin
from .models import OARole,OAUser,OAPermission

admin.site.register(OARole)
admin.site.register(OAUser)
admin.site.register(OAPermission)
