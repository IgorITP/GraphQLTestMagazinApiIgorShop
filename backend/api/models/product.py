from django.db.models import Model, ForeignKey, CharField, SlugField, TextField, DecimalField, PositiveIntegerField, \
    DateTimeField, BooleanField, CASCADE
from .category import Category


class Product(Model):
    category = ForeignKey(Category, related_name="products", default="", null=False, on_delete=CASCADE, blank=False)
    name = CharField(verbose_name="Name Product", default="", max_length=100, blank=False)
    slug = SlugField(verbose_name="Slug", default="", max_length=100, blank=False)
    description = TextField(verbose_name="Description", default="", max_length=100, blank=False)
    price = DecimalField(verbose_name='Price', default="", max_digits=10, decimal_places=2, blank=False)
    stock = PositiveIntegerField()
    available = BooleanField(default=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        index_together = (("id", 'slug'),)


