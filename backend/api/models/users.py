from django.db.models import CharField, Model, EmailField, DateTimeField
from django.utils.timezone import now


class Users(Model):
    username = CharField(verbose_name='Login', default="", max_length=100, blank=False)
    password = CharField(verbose_name="Password", default="", max_length=100, blank=False)
    email = EmailField(verbose_name="Email", default="", max_length=100, blank=False)
    first_name = CharField(verbose_name="Name", max_length=100, default="")
    create_at = DateTimeField(verbose_name="Registration Data", default=now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
