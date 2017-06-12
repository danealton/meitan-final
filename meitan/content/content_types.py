from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.encoding import python_2_unicode_compatible
from cloudinary.models import CloudinaryField
from common.content_types import RenderCTMixin
from redactor.fields import RedactorField
from feincms.admin.item_editor import FeinCMSInline
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from products.models import Product
from news.models import News




@python_2_unicode_compatible
class ProductsNewCT(RenderCTMixin, models.Model):
    template_name = "content\content_types\products_new.html"

    def get_template_data(self):
        products = Product.objects.all().order_by('-created')


        return {
            'ctx': {
                'products': products[:10],
            }
        }

    def __str__(self):
        return ugettext('ProductsNewCT block')

    class Meta:
        abstract = True
        verbose_name = _('ProductsNewCT')
        verbose_name_plural = _('ProductsNewCT')


@python_2_unicode_compatible
class ProductsRelated(RenderCTMixin, models.Model):
    template_name = "content\content_types\product_related.html"

    def get_template_data(self):
        products = Product.objects.all()

        return {
            'ctx': {
                'products': products[:10],
            }
        }

    def __str__(self):
        return ugettext('ProductsRelated block')

    class Meta:
        abstract = True
        verbose_name = _('ProductsRelated')
        verbose_name_plural = _('ProductsRelated')

@python_2_unicode_compatible
class NewsBlock(RenderCTMixin, models.Model):
    template_name = "content\content_types\snews_block.html"

    def get_template_data(self):
        news = News.objects.all().order_by('-date')


        return {
            'ctx': {
                'news': news[:10],
            }
        }

    def __str__(self):
        return ugettext('NewsBlock')

    class Meta:
        abstract = True
        verbose_name = _('NewsBlock')
        verbose_name_plural = _('NewsBlock')



