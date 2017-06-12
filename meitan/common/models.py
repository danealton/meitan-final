from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cloudinary.models import CloudinaryField
from common.utils import get_cloudinary_thumb
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from common.utils import get_cloudinary_thumb
# from spy_site.consts import THUMBNAILS_OPTS
# from .helpers import thmb_factory
from redactor.fields import RedactorField


# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class CommonPost(models.Model):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    # base grid fields
    title = models.CharField(
                max_length=255,
                verbose_name=_('title'),
                null=True,
    )

    subtitle = models.CharField(
                max_length=255,
                verbose_name=_('subitle'),
                null=True,
    )

    text = RedactorField(
        _('text'),
        allow_file_upload=False,
        allow_image_upload=False,
        blank=True,
        null=True
    )

    text_preview = models.CharField(
                max_length=1000,
                verbose_name=_('text_preview'),
                null=True,
    )

    date = models.DateField(_('date'), null=True)

    image = CloudinaryField(_('image'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('update at'))

    def get_admin_thumbnail(self):
        return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)



    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ('order',)


class Category(models.Model):
    title = models.CharField(blank=True, max_length=255, verbose_name=_('title'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, editable=False)

    def __str__(self):
        return ('-- ' if self.parent else '') + self.title

    class Meta:
        abstract = True
        ordering = ('tree_id', 'lft')


class CategoryItem(models.Model):
    title = models.CharField(blank=True, max_length=255, verbose_name=_('title'))
    price = models.CharField(blank=True, max_length=255, null=True, verbose_name=_('price'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ('order',)


class VideoFileMixin(models.Model):
    video_file = CloudinaryField(_('video file'), resource_type='video', null=True, blank=True)
    
    def get_video_tag(self):
        tag_data = {
            'webm_url': self.video_file.build_url(format = 'webm'),
            'mp4_url': self.video_file.build_url(format = 'mp4'),
            'ogg_url': self.video_file.build_url(format = 'ogg'),
            'cover': self.video_file.video_thumbnail(q=7)
        }
        return '''
            <div class="video-block" data-mp4="{webm_url}" 
                data-ogg="{mp4_url}"
                data-webm="{ogg_url}"
                style="background-image: url({cover})">
            </div>
        '''.format(**tag_data)
    
    class Meta:
        abstract = True