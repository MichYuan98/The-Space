from django.contrib import admin

# Register your models here.
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name']}),
            (None, {'fields': ['camera_ip_url']}),
            (None, {'fields': ['capacity']}),
            (None, {'fields': ['current_count']}),
            (None, {'fields': ['location']}),
            (None, {'fields': ['other_comments']})
                ]


admin.site.register(Room, RoomAdmin)
admin.site.site_url = "http://127.0.0.1:8000/flowControl"
