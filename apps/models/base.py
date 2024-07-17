from django.db.models import Model, CharField, SlugField, DateTimeField
from django.db.models.functions import Now
from django.utils.text import slugify


class SlugBasedModel(Model):
    class Meta:
        abstract = True

    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class CreatedBasedModel(Model):
    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())
