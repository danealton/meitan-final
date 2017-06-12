from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from feincms.apps import app_reverse
from mptt.fields import TreeForeignKey
from django.template.defaultfilters import slugify
from unidecode import unidecode


@python_2_unicode_compatible
class Sale(models.Model):

    content = models.TextField(
                max_length=1000,
                verbose_name=_('content'),
                null=True,
    )


    customer_name = models.CharField(
                max_length=255,
                verbose_name=_('customer_name'),
                null=True,
    )

    customer_adress = models.CharField(
                max_length=255,
                verbose_name=_('customer_adress'),
                null=True,
    )

    customer_phone = models.CharField(
                max_length=255,
                verbose_name=_('customer_phone'),
                null=True,
    )

    customer_email = models.CharField(
                max_length=255,
                verbose_name=_('customer_email'),
                null=True,
    )

    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _('Sale')
        verbose_name_plural = _('Sale')
        ordering = ('-created',)

    def __str__(self):
        return self.customer_name
