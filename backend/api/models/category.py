from django.db.models import Model, CharField, SlugField


class Category(Model):
    objects = None
    name = CharField(verbose_name="Name Category", default="", max_length=100, blank=False)
    slug = SlugField(verbose_name="Slug", default="", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
