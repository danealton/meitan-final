from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.translation import ugettext_lazy as _
from django_mptt_admin.admin import DjangoMpttAdmin
from django_mptt_admin.admin import DjangoMpttAdmin, MPTTModelAdmin
from feincms.admin.item_editor import FeinCMSInline
from django.utils.html import format_html
from .models import Sale
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib.sessions.models import Session


class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_adress', 'paid','delivered',)

    fieldsets = (
        (_('Sale'), {
            'fields': ('paid','delivered', 'content',),
        }),
    )

admin.site.register(Sale, SaleAdmin)
