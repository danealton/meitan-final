from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.translation import ugettext_lazy as _
from django_mptt_admin.admin import DjangoMpttAdmin
from django_mptt_admin.admin import DjangoMpttAdmin, MPTTModelAdmin
from feincms.admin.item_editor import FeinCMSInline
from django.utils.html import format_html
from .models import Category, Product
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib.sessions.models import Session

#from .form import NewMediaForm



class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

    fieldsets = (
        (_('Education'), {
            'fields': ('category','title','subtitle', 'amount', 'age', 'appoitment', 'skin', 'frequency',
                'perfume', 'consistency', 'packaging','country', 'image', 'description', 'price', 'recommended'),
        }),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
