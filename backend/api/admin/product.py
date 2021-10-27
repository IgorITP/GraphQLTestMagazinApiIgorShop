from django.contrib.admin import register, ModelAdmin
from ..models import Product


@register(Product)
class ProductAdminForm(ModelAdmin):
    list_display = ("name", "slug", "price", "stock", "available", "created", "updated")
    list_filter = ("available", "created", "updated")
    list_editable = ("price", "stock", "available")
    prepopulated_fields = {"slug": ("name",)}

