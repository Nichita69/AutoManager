from django.contrib import admin

from apps.Contact.models import Contact

from apps.common.admin import get_model_fields


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = get_model_fields
