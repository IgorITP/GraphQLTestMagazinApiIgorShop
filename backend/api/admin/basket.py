from django.contrib.admin import register, ModelAdmin
from ..models import Basket


@register(Basket)
class BasketAdminForm(ModelAdmin):
    list_display = ("user", "product", "quantity")
    list_display_links = ("user", "product", "quantity")
