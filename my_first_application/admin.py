from django.contrib import admin

from my_first_application.models import OverFirst


# admin.site.register(OverFirst)

@admin.register(OverFirst)
class OverFirstAdmin(admin.ModelAdmin):
    list_display = ['id', 'field_0', 'field_1', 'field_2', 'field_3']
