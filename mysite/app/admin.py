from django.contrib import admin

from . import models

admin.site.register(models.Server)


class RoleAdmin(admin.ModelAdmin):
    autocomplete_fields = ["members"]


admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.FriendRequest)
admin.site.register(models.DirectMessageChannel)
admin.site.register(models.DirectMessage)
admin.site.register(models.TextChannel)
