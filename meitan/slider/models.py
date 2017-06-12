from __future__ import unicode_literals
from django.db import models
from common.models import CommonPost
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.encoding import python_2_unicode_compatible
from common.utils import get_cloudinary_thumb



class IndexSlide(models.Model):

    image = CloudinaryField(_('image'))

    order = models.PositiveIntegerField(default=0, blank=False, null=False)


    class Meta:
        ordering = ['order',]
        verbose_name = _('IndexSlide')
        verbose_name_plural = _('IndexSlides')

    def get_admin_thumbnail(self):
            return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)

    def get_index_image(self):
        return get_cloudinary_thumb(self.image, width=1800, height=640, crop="fill", q=7)
