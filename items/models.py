from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class ItemCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=100, verbose_name=_("item name"))
    category = models.ForeignKey(ItemCategory, on_delete=models.RESTRICT,  verbose_name=_("category"))
    price = models.DecimalField(validators=[MinValueValidator(1)], max_digits=19, decimal_places=3, verbose_name=_("price"))
    quantity = models.IntegerField(validators=[MinValueValidator(1)], verbose_name=_("quantity"))
    necessity = models.TextField(verbose_name=_("necessity"))
    approval = models.BooleanField(default=False, verbose_name=_("approval"))
    item_code = models.CharField(null=True,blank=True,max_length=100, verbose_name=_("item code"))
    url = models.URLField(null=True,blank=True)
    priority = models.IntegerField(default=0, verbose_name=_("priority"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Registered Date"))
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name=_("Registered User")
    )

    def __str__(self):
        return self.item_name

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name=_("comment"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Registered Date"))
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name=_("Registered User")
    )

    def __str__(self):
        return self.comment
