import uuid

from django.contrib.postgres.functions import RandomUUID
from django.db.models import UUIDField, FloatField, ForeignKey, CASCADE, DateTimeField, \
    TextField, PositiveSmallIntegerField, ImageField
from django.db.models.functions import Now

from apps.models.base import SlugBasedModel


class Category(SlugBasedModel):
    # variant 2
    parent = ForeignKey('apps.Category', CASCADE, null=True, blank=True)

    # self yzosa boladi
    # parent = ForeignKey('self', CASCADE)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


#    variant 1
# class SubCategory(SlugBasedModel):
#     parent_category =ForeignKey('apps.Category',CASCADE)
#

class Product(SlugBasedModel):
    # class Meta:
    #
    id = UUIDField(primary_key=True, default=uuid.uuid4, db_default=RandomUUID(), editable=False)
    price = FloatField(help_text="price in UZB SO'M")
    image = ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True)
    description = TextField(blank=True, null=True)
    discount = PositiveSmallIntegerField(default=0, help_text='Chegirma foizi')
    category = ForeignKey('apps.Category', CASCADE)
    created_at = DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())

    @property
    def current_price(self):
        return self.price - self.price * self.discount / 100
