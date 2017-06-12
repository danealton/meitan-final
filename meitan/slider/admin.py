from django.contrib import admin
from .models import IndexSlide
from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.html import format_html
from common.admin import CommonPostAdmin
#from common.translation import GridPostTranslationOptions
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin





# Register your models here.
#def admin_thumbnail_img(obj):
#   return format_html('<img src=%s >' % obj.get_admin_thumbnail())
def get_admin_thumbnail(self):
        return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)

def admin_thumbnail_img(obj):
    return format_html('<img src=%s >' % obj.get_admin_thumbnail())


class IndexSlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id',admin_thumbnail_img )
    sortable = 'order'





admin.site.register(IndexSlide, IndexSlideAdmin)

