from django.contrib import admin
from .models import OARole


class OARoleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "desc", "ps_ids"]


admin.site.register(OARole, OARoleAdmin)
