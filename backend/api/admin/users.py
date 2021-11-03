from django.contrib.admin import register, ModelAdmin
from ..models import Users


@register(Users)
class UsersAdminForm(ModelAdmin):
    list_display = ("username", "email", "first_name", "create_at")
    list_display_links = ("email", "first_name", "username", "create_at")
    search_fields = ("email", "username")
