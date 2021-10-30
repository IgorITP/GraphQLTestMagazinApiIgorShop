from django.db.models import CharField, ForeignKey, Model, CASCADE
from .users import Users


class Basket(Model):
    user = ForeignKey(Users, related_name='basket', default="", null=False, on_delete=CASCADE, blank=False)
    product = CharField(verbose_name="Product", default="", max_length=100, blank=False)
    quantity = CharField(verbose_name="Quantity", default="", max_length=100, blank=False)

    def __str__(self):
        return self.user

    verbose_name = "Basket"
    verbose_name_plural = "Baskets"
