from __future__ import unicode_literals
from django.db import models
from common.models import CommonPost
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from common.utils import get_cloudinary_thumb
from django.utils import translation
from feincms.apps import app_reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from unidecode import unidecode
#from django.core.validators import RegexValidator, URLValidator


# Create your models here.
@python_2_unicode_compatible
class News(CommonPost):


    def get_admin_thumbnail(self):
        return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)

    def get_image_sm(self):
      return get_cloudinary_thumb(self.image, width=290, height=290, crop="fill", q=7)

    def get_absolute_url(self):
      return app_reverse('news_detail', 'news.urls', kwargs={
           'slug': self.slug,
        })

    slug = models.SlugField(blank=True, null=True)


    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(News, self).save()

    def __str__(self):
       return self.title

    class Meta:
      verbose_name = _('News')
      verbose_name_plural = _('News')
      ordering = ('-date',)

