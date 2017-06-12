from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
import mptt
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from feincms.apps import app_reverse
from mptt.fields import TreeForeignKey
from django.template.defaultfilters import slugify
from unidecode import unidecode
from common.utils import get_cloudinary_thumb

@python_2_unicode_compatible
class Category(models.Model):

    # main_categories = MainCategoriesManager()

    title = models.CharField(
                max_length=255,
                verbose_name=_('title'),
                null=True,
    )

    @staticmethod
    def get_main_categories():
        return Category.objects.filter(parent__isnull=True)

    def __str__(self):
        return self.title


	class Meta:
		verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('tree_id', 'lft')



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    title = models.CharField(
                max_length=255,
                verbose_name=_('title'),
                null=True,
    )
    subtitle = models.CharField(
                max_length=255,
                verbose_name=_('subtitle'),
                null=True,
    )
    amount = models.CharField(
                max_length=255,
                verbose_name=_('amount'),
                null=True,
    )
    age = models.CharField(
                max_length=255,
                verbose_name=_('age'),
                null=True,
    )
    appoitment = models.CharField(
                max_length=255,
                verbose_name=_('appoitment'),
                null=True,
    )
    skin = models.CharField(
                max_length=255,
                verbose_name=_('skin'),
                null=True,
    )
    frequency = models.CharField(
                max_length=255,
                verbose_name=_('frequency'),
                null=True,
    )
    perfume = models.CharField(
                max_length=255,
                verbose_name=_('perfume'),
                null=True,
    )
    consistency = models.CharField(
                max_length=255,
                verbose_name=_('consistency'),
                null=True,
    )
    packaging = models.CharField(
                max_length=255,
                verbose_name=_('packaging'),
                null=True,
    )
    country = models.CharField(
                max_length=255,
                verbose_name=_('country'),
                null=True,
    )
    slug = models.SlugField(max_length=200, db_index=True)
    image = CloudinaryField(_('image'))
    description = RedactorField(
        _('description'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True,
        null=True
    )
    contains = RedactorField(
        _('contains'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    recommended = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
      return app_reverse('products_detail', 'products.urls', kwargs={
           'slug': (self.slug),
        })

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Product, self).save()

    def get_image_sm(self):
        return get_cloudinary_thumb(self.image, width=350, height=210, crop="fill", q=7)

    def get_image_big(self):
        return get_cloudinary_thumb(self.image, width=700, height=400, crop="fill", q=7)






    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


TreeForeignKey(Category, blank=True, null=True, db_index=True).contribute_to_class(Category, 'parent')

mptt.register(Category, order_insertion_by=['title'])
