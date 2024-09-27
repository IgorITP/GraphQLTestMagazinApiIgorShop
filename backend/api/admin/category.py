from django.contrib.admin import register, ModelAdmin
from ..models import Category


@register(Category)
class CategoryAdminForm(ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
